from pyngrok import ngrok
import subprocess
import sys

def main():
    print("Starting Streamlit app with ngrok tunnel...")
    
    port = 8501
    public_url = ngrok.connect(port)
    
    print("\n" + "="*60)
    print(f"✅ Your app is now accessible at: {public_url}")
    print("="*60)
    print("\nShare this URL with students to access the app.")
    print("Press Ctrl+C to stop the server and close the tunnel.\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app/streamlit_app.py", "--server.port", str(port)])
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        ngrok.kill()

if __name__ == "__main__":
    main()