import os
from markitdown import MarkItDown, StreamInfo

def local_upload_handler(image_blob, meta):
    print(f"upload handler called for file: {meta['filename']}")
    """
    이미지 데이터를 로컬 폴더 'uploaded_images' 에 저장한 후,
    해당 파일이 정적 서버에서 제공된다고 가정하여 URL을 생성합니다.
    """
    
    current_dir = os.path.dirname(__file__)
    output_dir = os.path.join(current_dir, "uploaded_images")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"created directory: {output_dir}")

    
    output_file = os.path.join(output_dir, meta["filename"])
    with open(output_file, "wb") as f:
        f.write(image_blob)
        
    print(f"saved image to: {output_file}")

    
    url = f"http://localhost:8000/uploaded_images/{meta['filename']}"
    print(f"generated URL: {url}")
    return url


TEST_FILE_DIR = os.path.join(os.path.dirname(__file__), "test_files")
test_filename = "sample2.pptx" 
test_file_path = os.path.join(TEST_FILE_DIR, test_filename)

md = MarkItDown()

stream_info = StreamInfo(
    extension=".pptx",
    mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    charset=None
)

with open(test_file_path, "rb") as stream:
    result = md.convert(
        stream,
        stream_info=stream_info,
        # upload_handler=local_upload_handler,
        keep_data_uris=True
    )

print(result.markdown)
