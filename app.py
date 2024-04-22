import gradio as gr
import zipfile
import os


def process_file(file):
    if file.name.endswith((".png", ".jpg", ".jpeg")):
        zip_file_name = file.name + ".zip"
        with zipfile.ZipFile(zip_file_name, "w") as zipf:
            zipf.write(file.name)
        return "压缩文件保存地址: " + os.path.abspath(zip_file_name)
    elif file.name.endswith(".zip"):
        with zipfile.ZipFile(file.name, "r") as zip_ref:
            file_list = zip_ref.namelist()
        return (
            "压缩包文件列表: "
            + str(file_list)
            + "\n完整地址: "
            + os.path.abspath(file.name)
        )


iface = gr.Interface(fn=process_file, inputs="file", outputs="text")
iface.launch()
