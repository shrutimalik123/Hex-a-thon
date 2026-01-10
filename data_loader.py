import requests
import os

def download_data():
    url = "https://raw.githubusercontent.com/OSMIHelp/OSMI-2014-Mental-Health-in-Tech-Survey-Results/master/survey.csv"
    output_dir = "data"
    output_file = os.path.join(output_dir, "survey.csv")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    print(f"Attempting download from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for bad status codes
        
        with open(output_file, "wb") as f:
            f.write(response.content)
            
        print(f"Successfully downloaded to: {output_file}")
        print(f"File size: {os.path.getsize(output_file)} bytes")
        
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        # Fallback check - maybe it's 'main' instead of 'master'
        try:
             url = "https://raw.githubusercontent.com/OSMIHelp/OSMI-2014-Mental-Health-in-Tech-Survey-Results/main/survey.csv"
             print(f"Retrying with 'main' branch: {url}")
             response = requests.get(url)
             response.raise_for_status()
             with open(output_file, "wb") as f:
                f.write(response.content)
             print(f"Successfully downloaded to: {output_file}")
        except Exception as e2:
             print(f"Failed second attempt: {e2}")

if __name__ == "__main__":
    download_data()
