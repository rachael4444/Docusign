import urllib.parse

original_url = "https://audio.paradaconstrcution.com/"
first_encoded = urllib.parse.quote(original_url)
double_encoded = urllib.parse.quote(first_encoded)
redirect_url = f"https://www.google.com/url?q=https://www.google.com/url?q%3D{double_encoded}"

print("Redirect URL:", redirect_url)
