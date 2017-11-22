# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.0 for Linux x86 (64-bit) (September 9, 2014)
# Date: Sun 19 Nov 2017 16:19:45


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.b__tilde__):'(CKM2x3*ee**2*MW**4*complexconjugate(CKM2x3))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(CKM2x1*ee**2*MW**4*complexconjugate(CKM2x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(CKM2x2*ee**2*MW**4*complexconjugate(CKM2x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(CKM3x3*ee**2*MW**4*complexconjugate(CKM3x3))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.d__tilde__):'(CKM3x1*ee**2*MW**4*complexconjugate(CKM3x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.s__tilde__):'(CKM3x2*ee**2*MW**4*complexconjugate(CKM3x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.b__tilde__):'(CKM1x3*ee**2*MW**4*complexconjugate(CKM1x3))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(CKM1x1*ee**2*MW**4*complexconjugate(CKM1x1))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(CKM1x2*ee**2*MW**4*complexconjugate(CKM1x2))/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)'})

Decay_WR__plus__ = Decay(name = 'Decay_WR__plus__',
                         particle = P.WR__plus__,
                         partial_widths = {(P.c,P.b__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR2x3**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.c,P.d__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR2x1**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.c,P.s__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR2x2**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.t,P.b__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR3x3**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.t,P.d__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR3x1**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.t,P.s__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR3x2**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.u,P.b__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR1x3**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.u,P.d__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR1x1**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.u,P.s__tilde__):'(ee**2*kRq**2*MWR**4*VCKMR1x2**2)/(16.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.ve,P.e__plus__):'(ee**2*kRl**2*MWR**4*YlN1x1**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.ve,P.mu__plus__):'(ee**2*kRl**2*MWR**4*YlN1x2**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.ve,P.ta__plus__):'(ee**2*kRl**2*MWR**4*YlN1x3**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vm,P.e__plus__):'(ee**2*kRl**2*MWR**4*YlN2x1**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vm,P.mu__plus__):'(ee**2*kRl**2*MWR**4*YlN2x2**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vm,P.ta__plus__):'(ee**2*kRl**2*MWR**4*YlN2x3**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vt,P.e__plus__):'(ee**2*kRl**2*MWR**4*YlN3x1**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vt,P.mu__plus__):'(ee**2*kRl**2*MWR**4*YlN3x2**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)',
                                           (P.vt,P.ta__plus__):'(ee**2*kRl**2*MWR**4*YlN3x3**2)/(48.*cmath.pi*sw**2*abs(MWR)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

Decay_ZR = Decay(name = 'Decay_ZR',
                 particle = P.ZR,
                 partial_widths = {(P.b,P.b__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.c,P.c__tilde__):'(MZR**2*((6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.d,P.d__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.e__minus__,P.e__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.mu__minus__,P.mu__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.N1,P.N1):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN1**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN1**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.N2,P.N2):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN2**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN2**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.N3,P.N3):'(((-16*ee**2*gZRNL**2*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) + (32*ee**2*gZRNL*gZRNR*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) - (16*ee**2*gZRNR**2*kRl**2*kRl2*mN3**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) - (8*ee**2*gZRNL*gZRNR*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (4*ee**2*gZRNR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)))*cmath.sqrt(-4*mN3**2*MZR**2 + MZR**4))/(96.*cmath.pi*abs(MZR)**3)',
                                   (P.s,P.s__tilde__):'(MZR**2*((6*ee**2*gZRdL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRdR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.t,P.t__tilde__):'(MZR**2*((6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.ta__minus__,P.ta__plus__):'(MZR**2*((2*ee**2*gZReL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZReR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.u,P.u__tilde__):'(MZR**2*((6*ee**2*gZRuL**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2)) + (6*ee**2*gZRuR**2*kRq**2*kRq2*MZR**2)/(sw**2*(kRq2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.ve,P.ve__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.vm,P.vm__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)',
                                   (P.vt,P.vt__tilde__):'(MZR**2*((2*ee**2*gZRvL**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2)) + (2*ee**2*gZRvR**2*kRl**2*kRl2*MZR**2)/(sw**2*(kRl2 - tw2))))/(48.*cmath.pi*abs(MZR)**3)'})

