#!/usr/bin/env python3
import subprocess
import time
import requests
import sys

def test_server():
    print("Testing Flask application...")

    # Start the Flask app in background
    print("Starting Flask server...")
    process = subprocess.Popen(
        ["python", "application.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Wait for server to start
    time.sleep(5)

    try:
        # Test if server is running by checking the home page
        print("Testing home page...")
        response = requests.get("http://127.0.0.1:5000/", timeout=10)
        if response.status_code == 200:
            print("✅ Home page loaded successfully")
            print(f"Home page title: {response.text[:200]}...")
        else:
            print(f"❌ Home page failed with status code: {response.status_code}")

        # Test the FWI prediction page
        print("Testing FWI prediction page...")
        response = requests.get("http://127.0.0.1:5000/predictdata", timeout=10)
        if response.status_code == 200:
            print("✅ FWI prediction page loaded successfully")
        else:
            print(f"❌ FWI prediction page failed with status code: {response.status_code}")

        # Test the Fire Risk prediction page
        print("Testing Fire Risk prediction page...")
        response = requests.get("http://127.0.0.1:5000/predictfire", timeout=10)
        if response.status_code == 200:
            print("✅ Fire Risk prediction page loaded successfully")
            print("✅ All pages loaded successfully!")
            print("\n🎉 Application test completed!")
            print("The Flask server is running and serving the enhanced UI.")
        else:
            print(f"❌ Fire Risk prediction page failed with status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Server may not be running.")
    except requests.exceptions.Timeout:
        print("❌ Request timeout. Server may not be responding.")
    finally:
        # Kill the server process
        print("Stopping Flask server...")
        process.terminate()
        process.wait()
        print("✅ Server stopped successfully")

if __name__ == "__main__":
    test_server()