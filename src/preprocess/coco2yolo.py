from ultralytics.data.converter import convert_coco

# Укажите путь к вашему файлу с аннотациями в формате COCO
coco_annotations_path = "//home/rosalie/Desktop/livecell_bot/annotations"

# Выполняем конвертацию
convert_coco(labels_dir=coco_annotations_path, use_segments=True)
