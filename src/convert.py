import os
import shutil
from collections import defaultdict
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_ext, get_file_name, get_file_name_with_ext
from supervisely.io.json import load_json_file
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    ### Function should read local dataset and upload it to Supervisely project, then return project info.###
    images_path = "/home/alex/DATASETS/TODO/OPEDD/left"
    r_images_path = "/home/alex/DATASETS/TODO/OPEDD/right"
    anns_path = "/home/alex/DATASETS/TODO/OPEDD/devkit_opedd/devkit_OPEDD/annotations"
    batch_size = 30
    images_ext = ".png"
    ds_name = "left"

    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 1242  # image_np.shape[0]
        img_wight = 2208  # image_np.shape[1]

        image_name = get_file_name_with_ext(image_path)
        image_data = im_name_to_data.get(image_name)
        mask = np.zeros((img_height, img_wight))
        if image_data is not None:
            for curr_im_data in image_data:
                curr_coords_data = curr_im_data["shape_attributes"]
                person_id_value = int(curr_im_data["region_attributes"]["Person_id"])
                if person_id_value == -1:
                    continue
                # person_id = sly.Tag(person_id_meta, value=person_id_value)
                exterior = []
                x_coords = curr_coords_data["all_points_x"]
                y_coords = curr_coords_data["all_points_y"]
                for x, y in zip(x_coords, y_coords):
                    exterior.append([int(y), int(x)])
                poligon = sly.Polygon(exterior)
                temp_color = person_id_to_pixel.get(person_id_value)
                poligon.draw(mask, color=temp_color)
            for pixel in person_id_to_pixel.values():
                person_id_value = pixel_to_person_id.get(pixel)
                person_id = sly.Tag(person_id_meta, value=person_id_value)
                obj_mask = mask == pixel
                if len(np.unique(obj_mask)) == 1:
                    continue
                curr_bitmap = sly.Bitmap(obj_mask)
                label_poly = sly.Label(curr_bitmap, obj_class, tags=[person_id])
                labels.append(label_poly)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("person", sly.Bitmap)
    person_id_meta = sly.TagMeta("person id", sly.TagValueType.ANY_NUMBER)
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[person_id_meta])
    api.project.update_meta(project.id, meta.to_json())

    person_id_to_pixel = {
        0: 25,
        1: 50,
        2: 75,
        3: 100,
        4: 125,
        5: 150,
        6: 175,
        7: 200,
        8: 225,
        9: 250,
    }
    pixel_to_person_id = {
        25: 0,
        50: 1,
        75: 2,
        100: 3,
        125: 4,
        150: 5,
        175: 6,
        200: 7,
        225: 8,
        250: 9,
    }

    # im_name_to_data = defaultdict(list)

    # for ann_name in os.listdir(anns_path):
    #     ann_path = os.path.join(anns_path, ann_name)

    #     ann = load_json_file(ann_path)["_via_img_metadata"]
    #     for curr_ann_data in ann.values():
    #         im_name_to_data[curr_ann_data["filename"]].extend(curr_ann_data["regions"])

    # dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    # images_names = [
    #     im_name for im_name in os.listdir(images_path) if get_file_ext(im_name) == images_ext
    # ]

    # progress = sly.Progress("Add data to {} dataset".format(ds_name), len(images_names))

    # for img_names_batch in sly.batched(images_names, batch_size=batch_size):
    #     images_pathes_batch = [
    #         os.path.join(images_path, image_name) for image_name in img_names_batch
    #     ]

    #     img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
    #     img_ids = [im_info.id for im_info in img_infos]

    #     anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
    #     api.annotation.upload_anns(img_ids, anns_batch)

    #     progress.iters_done_report(len(img_names_batch))

    dataset = api.dataset.create(project.id, "right", change_name_if_conflict=True)

    images_names = [
        im_name for im_name in os.listdir(r_images_path) if get_file_ext(im_name) == images_ext
    ]

    progress = sly.Progress("Add data to right dataset", len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(r_images_path, image_name) for image_name in img_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
