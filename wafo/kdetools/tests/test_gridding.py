'''
Created on 23. des. 2016

@author: pab
'''
from __future__ import division
import unittest
import numpy as np
from numpy.testing import assert_allclose
from numpy import array
import wafo.kdetools.gridding as wkg


class TestKdeTools(unittest.TestCase):
    @staticmethod
    def test_gridcount_1d():
        # N = 20
        # data = np.random.rayleigh(1, size=(N,))
        # print(data.tolist())
        data = [0.6493244636902034, 0.6562823794215175, 1.0905183896319681,
                0.42206966930980305, 3.2401808457841033, 0.4527768130472434,
                1.2078346032213523, 0.7042615640603758, 1.1514223608901017,
                0.9233030250922233, 1.0709559676055374, 0.7132605765584901,
                0.6560730230166847, 0.734614714549834, 1.0404525505934663,
                0.6750474427282895, 0.8801082165600141, 1.7235435044161305,
                1.2660483754981589, 0.9811765136936577]
        x = np.linspace(0, max(data) + 1, 10)

        dx = x[1] - x[0]
        c = wkg.gridcount(data, x)
        assert_allclose(c,
                        [0.1430937435034, 5.864465648665, 9.418694957317207,
                         2.9154367000439, 0.6583089504704, 0.0,
                         0.12255097773682266, 0.8774490222631774, 0.0, 0.0])
        t = np.trapz(c / dx / len(data), x)
        assert_allclose(t, 0.9964226564124143)

    @staticmethod
    def test_gridcount_2d():
        N = 20
        # data = np.random.rayleigh(1, size=(2, N))
        data = array([
            [0.38103275, 0.35083136, 0.90024207, 1.88230239, 0.96815399,
             0.57392873, 1.63367908, 1.20944125, 2.03887811, 0.81789145,
             0.69302049, 1.40856592, 0.92156032, 2.14791432, 2.04373821,
             0.69800708, 0.58428735, 1.59128776, 2.05771405, 0.87021964],
            [1.44080694, 0.39973751, 1.331243, 2.48895822, 1.18894158,
             1.40526085, 1.01967897, 0.81196474, 1.37978932, 2.03334689,
             0.870329, 1.25106862, 0.5346619, 0.47541236, 1.51930093,
             0.58861519, 1.19780448, 0.81548296, 1.56859488, 1.60653533]])

        x = np.linspace(0, max(np.ravel(data)) + 1, 5)
        dx = x[1] - x[0]
        X = np.vstack((x, x))
        c = wkg.gridcount(data, X)
        assert_allclose(c,
                        [[0.38922806, 0.8987982,  0.34676493, 0.21042807,  0.],
                         [1.15012203, 5.16513541, 3.19250588, 0.55420752,  0.],
                         [0.74293418, 3.42517219, 1.97923195, 0.76076621,  0.],
                         [0.02063536, 0.31054405, 0.71865964, 0.13486633,  0.],
                         [0.,  0.,  0.,  0.,  0.]], 1e-5)

        t = np.trapz(np.trapz(c / (dx**2 * N), x), x)
        assert_allclose(t, 0.9011618785736376)

    @staticmethod
    def test_gridcount_3d():
        N = 20
        # data = np.random.rayleigh(1, size=(3, N))
        data = np.array([
            [0.932896, 0.89522635, 0.80636346, 1.32283371, 0.27125435,
             1.91666304, 2.30736635, 1.13662384, 1.73071287, 1.06061127,
             0.99598512, 2.16396591, 1.23458213, 1.12406686, 1.16930431,
             0.73700592, 1.21135139, 0.46671506, 1.3530304, 0.91419104],
            [0.62759088, 0.23988169, 2.04909823, 0.93766571, 1.19343762,
             1.94954931, 0.84687514, 0.49284897, 1.05066204, 1.89088505,
             0.840738, 1.02901457, 1.0758625, 1.76357967, 0.45792897,
             1.54488066, 0.17644313, 1.6798871, 0.72583514, 2.22087245],
            [1.69496432, 0.81791905, 0.82534709, 0.71642389, 0.89294732,
             1.66888649, 0.69036947, 0.99961448, 0.30657267, 0.98798713,
             0.83298728, 1.83334948, 1.90144186, 1.25781913, 0.07122458,
             2.42340852, 2.41342037, 0.87233305, 1.17537114, 1.69505988]])

        x = np.linspace(0, max(np.ravel(data)) + 1, 3)
        dx = x[1] - x[0]
        X = np.vstack((x, x, x))
        c = wkg.gridcount(data, X)
        assert_allclose(c,
                        [[[8.74229894e-01, 1.27910940e+00, 1.42033973e-01],
                          [1.94778915e+00, 2.59536282e+00, 3.28213680e-01],
                          [1.08429416e-01, 1.69571495e-01, 7.48896775e-03]],
                         [[1.44969128e+00, 2.58396370e+00, 2.45459949e-01],
                          [2.28951650e+00, 4.49653348e+00, 2.73167915e-01],
                          [1.10905565e-01, 3.18733817e-01, 1.12880816e-02]],
                         [[7.49265424e-02, 2.18142488e-01, 0.0],
                          [8.53886762e-02, 3.73415131e-01, 0.0],
                          [4.16196568e-04, 1.62218824e-02, 0.0]]])

        t = np.trapz(np.trapz(np.trapz(c / dx**3 / N, x), x), x)
        assert_allclose(t, 0.5164999727560187)

    @staticmethod
    def test_gridcount_4d():

        N = 20
        # data = np.random.rayleigh(1, size=(2, N))
        data = array([
            [0.38103275, 0.35083136, 0.90024207, 1.88230239, 0.96815399,
             0.57392873, 1.63367908, 1.20944125, 2.03887811, 0.81789145],
            [0.69302049, 1.40856592, 0.92156032, 2.14791432, 2.04373821,
             0.69800708, 0.58428735, 1.59128776, 2.05771405, 0.87021964],
            [1.44080694, 0.39973751, 1.331243, 2.48895822, 1.18894158,
                1.40526085, 1.01967897, 0.81196474, 1.37978932, 2.03334689],
            [0.870329, 1.25106862, 0.5346619, 0.47541236, 1.51930093,
                0.58861519, 1.19780448, 0.81548296, 1.56859488, 1.60653533]])

        x = np.linspace(0, max(np.ravel(data)) + 1, 3)
        dx = x[1] - x[0]
        X = np.vstack((x, x, x, x))
        c = wkg.gridcount(data, X)
        assert_allclose(c,
                        [[[[1.77163904e-01, 1.87720108e-01, 0.0],
                           [5.72573585e-01, 6.09557834e-01, 0.0],
                            [3.48549923e-03, 4.05931870e-02, 0.0]],
                            [[1.83770124e-01, 2.56357594e-01, 0.0],
                             [4.35845892e-01, 6.14958970e-01, 0.0],
                             [3.07662204e-03, 3.58312786e-02, 0.0]],
                            [[0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0],
                             [0.0, 0.0, 0.0]]],
                            [[[3.41883175e-01, 5.97977973e-01, 0.0],
                              [5.72071865e-01, 8.58566538e-01, 0.0],
                                [3.46939323e-03, 4.04056116e-02, 0.0]],
                             [[3.58861043e-01, 6.28962785e-01, 0.0],
                              [8.80697705e-01, 1.47373158e+00, 0.0],
                                [2.22868504e-01, 1.18008528e-01, 0.0]],
                             [[2.91835067e-03, 2.60268355e-02, 0.0],
                              [3.63686503e-02, 1.07959459e-01, 0.0],
                                [1.88555613e-02, 7.06358976e-03, 0.0]]],
                            [[[3.13810608e-03, 2.11731327e-02, 0.0],
                              [6.71606255e-03, 4.53139824e-02, 0.0],
                                [0.0, 0.0, 0.0]],
                             [[7.05946179e-03, 5.44614852e-02, 0.0],
                              [1.09099593e-01, 1.95935584e-01, 0.0],
                                [6.61257395e-02, 2.47717418e-02, 0.0]],
                             [[6.38695629e-04, 5.69610302e-03, 0.0],
                              [1.00358265e-02, 2.44053065e-02, 0.0],
                                [5.67244468e-03, 2.12498697e-03, 0.0]]]])

        t = np.trapz(np.trapz(np.trapz(np.trapz(c / dx**4 / N, x), x), x), x)
        assert_allclose(t, 0.21183518274521254)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
