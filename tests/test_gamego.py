import unittest
import random
from stubs.errors import PlayerIsDead
from stubs.gamego import main, initialize_state, finalize_state, set_alarm


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.state = {
            'user_id': random.randrange(255),
            'program': 'program',
        }

    def test_main(self):
        state = initialize_state(self.state, 'Phantom')
        self.assertEqual('The Phantom', state['globme'])

        state = initialize_state(self.state, 'username')
        self.assertEqual('username', state['globme'])

        old_state = {**state}
        self.assertEqual(old_state, state['onStop'](state))
        self.assertEqual(old_state, state['onError'](state))

        state = finalize_state(state)
        self.assertEqual(state['pr_due'], 0)

        # self.assertRaises(ValueError, main(self.state, 'username'))

    def test_sig_alon(self):
        state = set_alarm(self.state, True)
        self.assertTrue(state['sig_active'])
        self.assertFalse(state['__ignore'])
        self.assertEqual(2, state['__time'])

    def test_sig_aloff(self):
        state = set_alarm(self.state, False)
        self.assertFalse(state['sig_active'])
        self.assertTrue(state['__ignore'])
        self.assertFalse(state['__time'])

    def test_sig_occur(self):
        # state['onTime']  # onTime
        self.assertRaises(SystemExit, self.state['onTime']())

    def test_sig_oops(self):
        state = initialize_state(self.state, 'username')

        old_state = {**state}
        self.assertEqual(old_state, state['onStop'](state))
        self.assertEqual(old_state, state['onError'](state))

    def test_sig_ctrlc(self):
        state = initialize_state(self.state, 'username')

        state['in_fight'] = False
        self.assertRaises(PlayerIsDead, lambda: state['onQuit'](state))  # onQuit
        self.assertRaises(PlayerIsDead, lambda: state['onKill'](state))  # onQuit

        state['in_fight'] = True
        old_state = {**state}
        self.assertEqual(old_state, state['onQuit'](state))  # onQuit
        self.assertEqual(old_state, state['onKill'](state))  # onQuit


if __name__ == '__main__':
    unittest.main()
