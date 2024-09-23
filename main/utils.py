from bs4 import BeautifulSoup
import cloudinary.uploader

def process_content_images(content):
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all <img> tags in the content
    images = soup.find_all('img')
    
    for img in images:
        # Extract the image source
        img_src = img['src']
        
        # Check if the src is a local file (not a Cloudinary URL)
        if "res.cloudinary.com" in img_src:
            # Upload the image to Cloudinary
            response = cloudinary.uploader.upload(img_src, folder='Blog/content')
            
            # Replace the image source with the Cloudinary URL
            img['src'] = response['url']
            print(img['src'])
            
    
    # Return the updated content as a string
    return str(soup)
