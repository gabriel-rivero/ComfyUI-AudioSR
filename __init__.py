try:
    from .vasr_node import NODE_CLASS_MAPPINGS as _vasr_mappings
    from .vasr_node import NODE_DISPLAY_NAME_MAPPINGS as _vasr_display
except ImportError:
    _vasr_mappings = {}
    _vasr_display = {}

try:
    from .model_loader import AudioSRModelLoader
    from .sampler_node import AudioSRSampler
    _new_nodes = {
        "AudioSRModelLoader": AudioSRModelLoader,
        "AudioSRSampler": AudioSRSampler,
    }
    _new_display = {
        "AudioSRModelLoader": "AudioSR / FlashSR Model Loader",
        "AudioSRSampler": "AudioSR / FlashSR Sampler",
    }
except Exception as e:
    print(f"[ComfyUI-AudioSR] FlashSR nodes not loaded: {e}")
    _new_nodes = {}
    _new_display = {}

NODE_CLASS_MAPPINGS = {**_vasr_mappings, **_new_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {**_vasr_display, **_new_display}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
