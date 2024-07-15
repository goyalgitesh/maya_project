import asyncio
from src.facial_recognition import FacialRecognitionSystem
from src.dynamic_interactivity import OutfitVisualizer, Animator
from src.voice_interaction import VoiceInteractionSystem
from src.ar_integration import AREngine
from src.backend.app import create_app

async def main():
    # Initialize components
    facial_rec = FacialRecognitionSystem()
    outfit_vis = OutfitVisualizer()
    animator = Animator()
    voice_system = VoiceInteractionSystem()
    ar_engine = AREngine()
    
    # Start the backend server
    app = create_app()
    
    # Run all systems concurrently
    await asyncio.gather(
        facial_rec.run(),
        outfit_vis.run(),
        animator.run(),
        voice_system.run(),
        ar_engine.run(),
        app.run_task()
    )

if __name__ == "__main__":
    asyncio.run(main())