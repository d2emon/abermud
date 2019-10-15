import unittest
import random
from stubs import state
from stubs.errors import PlayerIsDead
from stubs.gamego import main, initialize_state, finalize_state, set_alarm


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.state = {
            'user_id': random.randrange(255),
            'program': 'program',
            **state,
        }

    def test_main(self):
        self.state = initialize_state(self.state, 'Phantom')
        self.assertEqual('The Phantom', self.state['name'])

        self.state = initialize_state(self.state, 'username')
        self.assertEqual('username', self.state['name'])

        old_state = {**self.state}
        self.assertEqual(old_state, self.state['onStop'](self.state))
        self.assertEqual(old_state, self.state['onError'](self.state))

        self.state = finalize_state(self.state)
        self.assertEqual(self.state['pr_due'], 0)

        # self.assertRaises(ValueError, main(self.state, 'username'))

    def test_sig_alon(self):
        self.state = set_alarm(self.state, True)
        self.assertTrue(self.state['timer_active'])
        self.assertFalse(self.state['__ignore'])
        self.assertEqual(2, self.state['__time'])

    def test_sig_aloff(self):
        self.state = set_alarm(self.state, False)
        self.assertFalse(self.state['timer_active'])
        self.assertTrue(self.state['__ignore'])
        self.assertFalse(self.state['__time'])

    def test_sig_occur(self):
        # state['onTime']  # onTime
        self.assertRaises(SystemExit, self.state['onTime'](state))

    def test_sig_oops(self):
        self.state = initialize_state(self.state, 'username')

        old_state = {**self.state}
        self.assertEqual(old_state, self.state['onStop'](self.state))
        self.assertEqual(old_state, self.state['onError'](self.state))

    def test_sig_ctrlc(self):
        self.state = initialize_state(self.state, 'username')

        self.state['in_fight'] = False
        self.assertRaises(PlayerIsDead, lambda: self.state['onQuit'](self.state))  # onQuit
        self.assertRaises(PlayerIsDead, lambda: self.state['onKill'](self.state))  # onQuit

        self.state['in_fight'] = True
        old_state = {**self.state}
        self.assertEqual(old_state, self.state['onQuit'](self.state))  # onQuit
        self.assertEqual(old_state, self.state['onKill'](self.state))  # onQuit


if __name__ == '__main__':
    unittest.main()
