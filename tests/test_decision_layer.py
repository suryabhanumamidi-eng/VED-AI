from Backend.Model import DecisionLayer


def test_image_generation_route():
    brain = DecisionLayer()
    result = brain.route_query("Generate image of neon city skyline")
    assert "Generating an image for:" in result or "Image generation request queued" in result


def test_demo_route_includes_both_responses():
    brain = DecisionLayer()
    result = brain.route_query("demo")
    assert "Demo Mode Initiated" in result
    assert "AI Response:" in result
    assert "Image Response:" in result
