import unittest
import random
from stubs import state, key
from stubs.gamego import initialize_state


class KeyTestCase(unittest.TestCase):
    def setUp(self):
        self.state = initialize_state(
            {
                'user_id': random.randrange(255),
                'program': 'program',
                **state,
            },
            'username',
        )

    def test_key_input(self):
        self.state['pr_due'] = True
        self.state = key.key_input(self.state, 'prompt', 128)
        self.assertFalse(self.state['pr_due'])
        self.assertLessEqual(128, self.state['key_buff'])
        self.assertEqual('text', self.state['key_buff'])

    def test_key_reprint(self):
        self.state['pr_qcr'] = False
        self.state['pr_due'] = True
        self.state = key.key_reprint(self.state)
        self.assertTrue(self.state['pr_qcr'])
        self.assertFalse(self.state['pr_due'])


if __name__ == '__main__':
    unittest.main()
