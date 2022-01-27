from imagekitio import ImageKit 

imagekit = ImageKit(
    private_key='private_lZ2TBYgMSGcC3gGuQGzGK5xsczM=',

    public_key='public_qsv1i9fzsRkkzkiFspK3NAjbUSo=',

    url_endpoint='https://ik.imagekit.io/wdjnrplts'
)

upload = imagekit.upload(
    file=open("opencv_frame_eldho.png", "rb"),
    file_name="opencv_frame_eldho.png",
    options={
        "response_fields": ["is_private_file", "tags"],
        "tags": ["tag1", "tag2"],
         "folder" : "/COVID-TRACER/"
    },
)
url = upload['response']['url']
print(url)
