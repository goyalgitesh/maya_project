import bpy
import asyncio

class Animator:
    def __init__(self):
        self.model = bpy.data.objects['HumanModel']

    async def animate_model(self, action_name):
        action = bpy.data.actions[action_name]
        if self.model.animation_data is None:
            self.model.animation_data_create()
        self.model.animation_data.action = action

    async def play_animation(self, start_frame, end_frame):
        bpy.context.scene.frame_start = start_frame
        bpy.context.scene.frame_end = end_frame
        bpy.ops.screen.animation_play()

    async def create_keyframe(self, frame, location, rotation):
        self.model.location = location
        self.model.rotation_euler = rotation
        self.model.keyframe_insert(data_path="location", frame=frame)
        self.model.keyframe_insert(data_path="rotation_euler", frame=frame)

    async def run(self):
        while True:
            # This is a placeholder for continuous animation
            # In a real scenario, this would interface with user input or other systems
            await asyncio.sleep(1/30)  # Animate at 30 FPS