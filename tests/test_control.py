import unittest

from uuv_mission.control import PDController

class TestPDController(unittest.TestCase):
    def test_compute_action(self):
        """Test that the compute_action method returns the expected action"""
        controller = PDController(kp=0.2, kd=0.5)
        reference = 10.0
        depth = 8.0
        action = controller.compute_action(reference, depth)
        expected_action = 0.2 * (reference - depth) + 0.5 * ((reference - depth) - 0.0)
        self.assertAlmostEqual(action, expected_action)

    def test_first_action_sets_previous_error(self):
        """Test that the first call to compute_action sets the previous_error correctly"""
        controller = PDController(kp=0.2, kd=0.5)
        reference = 10.0
        depth = 8.0
        controller.compute_action(reference, depth)
        self.assertEqual(controller.previous_error, reference - depth)

    def test_reset(self):
        """Test that the reset method restors initial behaviour of controller"""
        controller = PDController()

        controller.compute_action(reference=2.0, depth=1.0)
        controller.reset()
        action = controller.compute_action(reference=2.0, depth=1.0)

        self.assertAlmostEqual(action, 0.75)