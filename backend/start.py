#!/usr/bin/env python3
"""
Startup script for debugging deployment issues
"""
import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_environment():
    """Check if all required environment variables are set"""
    required_vars = ["GROQ_API_KEY", "PINECONE_API_KEY", "PINECONE_INDEX"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
        else:
            logger.info(f"✓ {var} is set")
    
    if missing_vars:
        logger.error(f"✗ Missing environment variables: {missing_vars}")
        return False
    
    logger.info("✓ All required environment variables are set")
    return True

def check_imports():
    """Check if all required packages can be imported"""
    try:
        import fastapi
        logger.info("✓ FastAPI imported successfully")
    except ImportError as e:
        logger.error(f"✗ Failed to import FastAPI: {e}")
        return False
    
    try:
        import uvicorn
        logger.info("✓ Uvicorn imported successfully")
    except ImportError as e:
        logger.error(f"✗ Failed to import Uvicorn: {e}")
        return False
    
    try:
        from pinecone import Pinecone
        logger.info("✓ Pinecone imported successfully")
    except ImportError as e:
        logger.error(f"✗ Failed to import Pinecone: {e}")
        return False
    
    try:
        from groq import Groq
        logger.info("✓ Groq imported successfully")
    except ImportError as e:
        logger.error(f"✗ Failed to import Groq: {e}")
        return False
    
    return True

def main():
    """Main startup check"""
    logger.info("Starting deployment checks...")
    
    # Check environment variables
    env_ok = check_environment()
    
    # Check imports
    imports_ok = check_imports()
    
    if env_ok and imports_ok:
        logger.info("✓ All checks passed! Starting application...")
        # Import and start the app
        try:
            from main import app
            import uvicorn
            
            port = int(os.getenv("PORT", 8000))
            logger.info(f"Starting server on port {port}")
            
            uvicorn.run(
                app,
                host="0.0.0.0",
                port=port,
                log_level="info"
            )
        except Exception as e:
            logger.error(f"✗ Failed to start application: {e}")
            sys.exit(1)
    else:
        logger.error("✗ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 