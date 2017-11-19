# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 10.0 for Linux x86 (64-bit) (September 9, 2014)
# Date: Sun 19 Nov 2017 16:19:45



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

YlN1x1 = Parameter(name = 'YlN1x1',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{YlN1x1}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 1, 1 ])

YlN1x2 = Parameter(name = 'YlN1x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN1x2}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 1, 2 ])

YlN1x3 = Parameter(name = 'YlN1x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN1x3}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 1, 3 ])

YlN2x1 = Parameter(name = 'YlN2x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN2x1}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 2, 1 ])

YlN2x2 = Parameter(name = 'YlN2x2',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{YlN2x2}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 2, 2 ])

YlN2x3 = Parameter(name = 'YlN2x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN2x3}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 2, 3 ])

YlN3x1 = Parameter(name = 'YlN3x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN3x1}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 3, 1 ])

YlN3x2 = Parameter(name = 'YlN3x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{YlN3x2}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 3, 2 ])

YlN3x3 = Parameter(name = 'YlN3x3',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = '\\text{YlN3x3}',
                   lhablock = 'LeptonMixingYlN',
                   lhacode = [ 3, 3 ])

Delt11 = Parameter(name = 'Delt11',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{Subsuperscript}[\\delta ,11,q]',
                   lhablock = 'Parameter',
                   lhacode = [ 1 ])

Delt12 = Parameter(name = 'Delt12',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{Subsuperscript}[\\delta ,12,q]',
                   lhablock = 'Parameter',
                   lhacode = [ 2 ])

Delt13 = Parameter(name = 'Delt13',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{Subsuperscript}[\\delta ,13,q]',
                   lhablock = 'Parameter',
                   lhacode = [ 3 ])

Delt21 = Parameter(name = 'Delt21',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{Subsuperscript}[\\delta ,21,q]',
                   lhablock = 'Parameter',
                   lhacode = [ 4 ])

Delt31 = Parameter(name = 'Delt31',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{Subsuperscript}[\\delta ,31,q]',
                   lhablock = 'Parameter',
                   lhacode = [ 5 ])

Delts = Parameter(name = 'Delts',
                  nature = 'external',
                  type = 'real',
                  value = -1.,
                  texname = '\\text{Subsuperscript}[\\delta ,s,q]',
                  lhablock = 'Parameter',
                  lhacode = [ 6 ])

Deltb = Parameter(name = 'Deltb',
                  nature = 'external',
                  type = 'real',
                  value = 0.01,
                  texname = '\\text{Subsuperscript}[\\delta ,b,q]',
                  lhablock = 'Parameter',
                  lhacode = [ 7 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.94,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000117456,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

VCKM11 = Parameter(name = 'VCKM11',
                   nature = 'external',
                   type = 'real',
                   value = 0.97427,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},11,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 1 ])

VCKM12 = Parameter(name = 'VCKM12',
                   nature = 'external',
                   type = 'real',
                   value = 0.2252,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},12,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 2 ])

VCKM13 = Parameter(name = 'VCKM13',
                   nature = 'external',
                   type = 'real',
                   value = 0.00867,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},13,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 3 ])

VCKM21 = Parameter(name = 'VCKM21',
                   nature = 'external',
                   type = 'real',
                   value = 0.22534,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},21,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 4 ])

VCKM22 = Parameter(name = 'VCKM22',
                   nature = 'external',
                   type = 'real',
                   value = 0.97344,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},22,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 5 ])

VCKM23 = Parameter(name = 'VCKM23',
                   nature = 'external',
                   type = 'real',
                   value = 0.0404,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},23,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 6 ])

VCKM31 = Parameter(name = 'VCKM31',
                   nature = 'external',
                   type = 'real',
                   value = 0.00351,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},31,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 7 ])

VCKM32 = Parameter(name = 'VCKM32',
                   nature = 'external',
                   type = 'real',
                   value = 0.0412,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},32,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 8 ])

VCKM33 = Parameter(name = 'VCKM33',
                   nature = 'external',
                   type = 'real',
                   value = 0.999146,
                   texname = '\\text{Subsuperscript}[\\text{VCKM},33,q]',
                   lhablock = 'VCKM',
                   lhacode = [ 9 ])

kRq = Parameter(name = 'kRq',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{Subsuperscript}[k,R,q]',
                lhablock = 'VRCOUP',
                lhacode = [ 1 ])

kRl = Parameter(name = 'kRl',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = '\\text{Subsuperscript}[k,R,l]',
                lhablock = 'VRCOUP',
                lhacode = [ 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.7,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MZR = Parameter(name = 'MZR',
                nature = 'external',
                type = 'real',
                value = 5070.,
                texname = '\\text{MZR}',
                lhablock = 'MASS',
                lhacode = [ 32 ])

MWR = Parameter(name = 'MWR',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MWR}',
                lhablock = 'MASS',
                lhacode = [ 34 ])

mN1 = Parameter(name = 'mN1',
                nature = 'external',
                type = 'real',
                value = 173.3,
                texname = '\\text{mN1}',
                lhablock = 'MASS',
                lhacode = [ 9900012 ])

mN2 = Parameter(name = 'mN2',
                nature = 'external',
                type = 'real',
                value = 1000000000000,
                texname = '\\text{mN2}',
                lhablock = 'MASS',
                lhacode = [ 9900014 ])

mN3 = Parameter(name = 'mN3',
                nature = 'external',
                type = 'real',
                value = 100000000000000,
                texname = '\\text{mN3}',
                lhablock = 'MASS',
                lhacode = [ 9900016 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00417,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WZR = Parameter(name = 'WZR',
                nature = 'external',
                type = 'real',
                value = 114.,
                texname = '\\text{WZR}',
                lhablock = 'DECAY',
                lhacode = [ 32 ])

WWR = Parameter(name = 'WWR',
                nature = 'external',
                type = 'real',
                value = 84.3,
                texname = '\\text{WWR}',
                lhablock = 'DECAY',
                lhacode = [ 34 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 2.12e-8,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 9900012 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 9900014 ])

WN3 = Parameter(name = 'WN3',
                nature = 'external',
                type = 'real',
                value = 100,
                texname = '\\text{WN3}',
                lhablock = 'DECAY',
                lhacode = [ 9900016 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

Delt22 = Parameter(name = 'Delt22',
                   nature = 'internal',
                   type = 'complex',
                   value = '1. - Delts**2',
                   texname = '\\text{Delt22}')

Delt23 = Parameter(name = 'Delt23',
                   nature = 'internal',
                   type = 'real',
                   value = 'Deltb*Delts',
                   texname = '\\text{Delt23}')

Delt32 = Parameter(name = 'Delt32',
                   nature = 'internal',
                   type = 'real',
                   value = 'Deltb*Delts',
                   texname = '\\text{Delt32}')

Delt33 = Parameter(name = 'Delt33',
                   nature = 'internal',
                   type = 'real',
                   value = '1. - Deltb**2',
                   texname = '\\text{Delt33}')

gZRNL = Parameter(name = 'gZRNL',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{gZRNL}')

gZRNR = Parameter(name = 'gZRNR',
                  nature = 'internal',
                  type = 'real',
                  value = '0.5',
                  texname = '\\text{gZRNR}')

gZRvR = Parameter(name = 'gZRvR',
                  nature = 'internal',
                  type = 'real',
                  value = '0',
                  texname = '\\text{gZRvR}')

kRl2 = Parameter(name = 'kRl2',
                 nature = 'internal',
                 type = 'real',
                 value = 'kRl**2',
                 texname = '\\text{kRl2}')

kRq2 = Parameter(name = 'kRq2',
                 nature = 'internal',
                 type = 'real',
                 value = 'kRq**2',
                 texname = '\\text{kRq2}')

VCKMR1x1 = Parameter(name = 'VCKMR1x1',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt11*VCKM11 + Delt21*VCKM12 + Delt31*VCKM13',
                     texname = '\\text{VCKMR1x1}')

VCKMR2x1 = Parameter(name = 'VCKMR2x1',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt11*VCKM21 + Delt21*VCKM22 + Delt31*VCKM23',
                     texname = '\\text{VCKMR2x1}')

VCKMR3x1 = Parameter(name = 'VCKMR3x1',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt11*VCKM31 + Delt21*VCKM32 + Delt31*VCKM33',
                     texname = '\\text{VCKMR3x1}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

VCKMR1x2 = Parameter(name = 'VCKMR1x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Delt12*VCKM11 + Delt22*VCKM12 + Delt32*VCKM13',
                     texname = '\\text{VCKMR1x2}')

VCKMR1x3 = Parameter(name = 'VCKMR1x3',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt13*VCKM11 + Delt23*VCKM12 + Delt33*VCKM13',
                     texname = '\\text{VCKMR1x3}')

VCKMR2x2 = Parameter(name = 'VCKMR2x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Delt12*VCKM21 + Delt22*VCKM22 + Delt32*VCKM23',
                     texname = '\\text{VCKMR2x2}')

VCKMR2x3 = Parameter(name = 'VCKMR2x3',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt13*VCKM21 + Delt23*VCKM22 + Delt33*VCKM23',
                     texname = '\\text{VCKMR2x3}')

VCKMR3x2 = Parameter(name = 'VCKMR3x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'Delt12*VCKM31 + Delt22*VCKM32 + Delt32*VCKM33',
                     texname = '\\text{VCKMR3x2}')

VCKMR3x3 = Parameter(name = 'VCKMR3x3',
                     nature = 'internal',
                     type = 'real',
                     value = 'Delt13*VCKM31 + Delt23*VCKM32 + Delt33*VCKM33',
                     texname = '\\text{VCKMR3x3}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

tw2 = Parameter(name = 'tw2',
                nature = 'internal',
                type = 'real',
                value = 'sw2/(1 - sw2)',
                texname = '\\text{tw2}')

gZRdL = Parameter(name = 'gZRdL',
                  nature = 'internal',
                  type = 'real',
                  value = '-tw2/(6.*kRq2)',
                  texname = '\\text{gZRdL}')

gZRdR = Parameter(name = 'gZRdR',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.5 + tw2/(3.*kRq2)',
                  texname = '\\text{gZRdR}')

gZReL = Parameter(name = 'gZReL',
                  nature = 'internal',
                  type = 'real',
                  value = 'tw2/(2.*kRl2)',
                  texname = '\\text{gZReL}')

gZReR = Parameter(name = 'gZReR',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.5 + tw2/kRl2',
                  texname = '\\text{gZReR}')

gZRuL = Parameter(name = 'gZRuL',
                  nature = 'internal',
                  type = 'real',
                  value = '-tw2/(6.*kRq2)',
                  texname = '\\text{gZRuL}')

gZRuR = Parameter(name = 'gZRuR',
                  nature = 'internal',
                  type = 'real',
                  value = '0.5 - (2*tw2)/(3.*kRq2)',
                  texname = '\\text{gZRuR}')

gZRvL = Parameter(name = 'gZRvL',
                  nature = 'internal',
                  type = 'real',
                  value = 'tw2/(2.*kRl2)',
                  texname = '\\text{gZRvL}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

