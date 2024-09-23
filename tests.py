# settings.py
import cloudinary
import cloudinary.uploader
import cloudinary.api	


cloudinary.config( 
  	cloud_name = "dpyxbvcyl",
  	api_key = "189186334241265",
  	api_secret = "sRuXkKXdLMwvMW_jlUqmOhPAGVk"
)

result = cloudinary.uploader.upload(
    "lockscreen1.png",
    asset_folder="Blog_images",
    resource_type="image")

url = result["url"]
print(url)