from pyngrok import ngrok, conf
import subprocess
import sys

def main():
    print("Starting Streamlit app with ngrok tunnel...")
    
    conf.get_default().auth_token = "36tiIU6MjTMfVrLButtMXuoY8xt_62AL2mYjb17Z3G8p7Vokw"
    
    port = 8501
    public_url = ngrok.connect(port)
    
    print("\n" + "="*60)
    print(f"✅ Your app is now accessible at: {public_url}")
    print("="*60)
    print("\nThis URL is now sharable and accessible from anywhere!")
    print("Press Ctrl+C to stop the server and close the tunnel.\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app/streamlit_app.py", "--server.port", str(port)])
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        ngrok.kill()

if __name__ == "__main__":
    main()