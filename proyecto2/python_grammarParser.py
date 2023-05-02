# Generated from python_grammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,558,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,3,0,59,8,0,1,1,1,1,1,1,1,2,1,2,5,2,66,8,2,10,2,
        12,2,69,9,2,1,2,1,2,1,3,1,3,3,3,75,8,3,1,4,1,4,1,4,1,4,3,4,81,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,91,8,5,1,6,1,6,1,6,3,6,96,
        8,6,1,6,1,6,1,6,3,6,101,8,6,1,7,1,7,1,7,1,7,5,7,107,8,7,10,7,12,
        7,110,9,7,1,7,1,7,1,7,3,7,115,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,140,8,11,1,11,1,11,1,11,1,11,3,11,146,8,11,5,11,148,
        8,11,10,11,12,11,151,9,11,3,11,153,8,11,1,11,1,11,1,11,1,11,3,11,
        159,8,11,1,11,1,11,1,11,4,11,164,8,11,11,11,12,11,165,1,12,1,12,
        1,12,1,12,5,12,172,8,12,10,12,12,12,175,9,12,1,12,1,12,1,12,1,12,
        3,12,181,8,12,1,13,1,13,1,13,3,13,186,8,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,194,8,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,202,8,13,
        5,13,204,8,13,10,13,12,13,207,9,13,3,13,209,8,13,1,13,1,13,3,13,
        213,8,13,1,13,1,13,1,13,1,13,1,13,3,13,220,8,13,1,13,1,13,1,13,3,
        13,225,8,13,1,13,1,13,1,13,1,13,1,13,3,13,232,8,13,5,13,234,8,13,
        10,13,12,13,237,9,13,3,13,239,8,13,1,13,1,13,1,14,1,14,3,14,245,
        8,14,1,14,1,14,3,14,249,8,14,1,14,1,14,1,15,1,15,1,15,3,15,256,8,
        15,1,15,1,15,1,16,1,16,5,16,262,8,16,10,16,12,16,265,9,16,1,16,1,
        16,1,16,3,16,270,8,16,1,17,1,17,1,17,1,17,5,17,276,8,17,10,17,12,
        17,279,9,17,3,17,281,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        290,8,17,1,17,1,17,1,17,3,17,295,8,17,1,18,1,18,1,18,1,18,5,18,301,
        8,18,10,18,12,18,304,9,18,3,18,306,8,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,3,18,315,8,18,1,18,1,18,1,18,3,18,320,8,18,1,19,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,5,20,332,8,20,10,20,12,20,
        335,9,20,3,20,337,8,20,1,20,1,20,1,20,1,20,1,20,1,20,5,20,345,8,
        20,10,20,12,20,348,9,20,3,20,350,8,20,1,20,1,20,1,20,1,20,1,20,1,
        20,5,20,358,8,20,10,20,12,20,361,9,20,3,20,363,8,20,1,20,1,20,1,
        20,1,20,1,20,1,20,5,20,371,8,20,10,20,12,20,374,9,20,3,20,376,8,
        20,1,20,3,20,379,8,20,1,21,1,21,1,21,5,21,384,8,21,10,21,12,21,387,
        9,21,1,21,1,21,1,21,1,21,5,21,393,8,21,10,21,12,21,396,9,21,3,21,
        398,8,21,1,21,3,21,401,8,21,1,21,1,21,1,21,5,21,406,8,21,10,21,12,
        21,409,9,21,1,21,1,21,1,21,1,21,3,21,415,8,21,1,22,1,22,1,22,3,22,
        420,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        432,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,455,8,23,
        10,23,12,23,458,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,471,8,24,1,25,1,25,1,25,5,25,476,8,25,10,25,12,25,
        479,9,25,3,25,481,8,25,1,25,1,25,1,25,1,25,1,25,5,25,488,8,25,10,
        25,12,25,491,9,25,3,25,493,8,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,5,26,502,8,26,10,26,12,26,505,9,26,3,26,507,8,26,1,26,1,26,1,
        26,1,26,1,26,5,26,514,8,26,10,26,12,26,517,9,26,3,26,519,8,26,1,
        26,1,26,1,26,1,26,1,26,5,26,526,8,26,10,26,12,26,529,9,26,3,26,531,
        8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,540,8,26,1,26,1,26,
        1,26,3,26,545,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,556,8,27,1,27,0,1,46,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,0,7,1,0,15,17,1,0,13,14,
        1,0,9,12,1,0,7,8,1,0,30,31,1,0,47,48,2,0,46,47,49,49,647,0,58,1,
        0,0,0,2,60,1,0,0,0,4,67,1,0,0,0,6,74,1,0,0,0,8,80,1,0,0,0,10,90,
        1,0,0,0,12,92,1,0,0,0,14,102,1,0,0,0,16,116,1,0,0,0,18,121,1,0,0,
        0,20,128,1,0,0,0,22,133,1,0,0,0,24,180,1,0,0,0,26,185,1,0,0,0,28,
        242,1,0,0,0,30,252,1,0,0,0,32,269,1,0,0,0,34,294,1,0,0,0,36,319,
        1,0,0,0,38,321,1,0,0,0,40,378,1,0,0,0,42,414,1,0,0,0,44,416,1,0,
        0,0,46,431,1,0,0,0,48,470,1,0,0,0,50,480,1,0,0,0,52,544,1,0,0,0,
        54,555,1,0,0,0,56,59,3,2,1,0,57,59,3,4,2,0,58,56,1,0,0,0,58,57,1,
        0,0,0,59,1,1,0,0,0,60,61,3,6,3,0,61,62,5,52,0,0,62,3,1,0,0,0,63,
        66,3,6,3,0,64,66,5,52,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,69,1,0,
        0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,71,
        5,0,0,1,71,5,1,0,0,0,72,75,3,10,5,0,73,75,3,8,4,0,74,72,1,0,0,0,
        74,73,1,0,0,0,75,7,1,0,0,0,76,81,3,14,7,0,77,81,3,16,8,0,78,81,3,
        18,9,0,79,81,3,22,11,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,
        80,79,1,0,0,0,81,9,1,0,0,0,82,91,3,12,6,0,83,91,3,20,10,0,84,91,
        3,24,12,0,85,91,3,28,14,0,86,87,3,48,24,0,87,88,5,52,0,0,88,91,1,
        0,0,0,89,91,5,53,0,0,90,82,1,0,0,0,90,83,1,0,0,0,90,84,1,0,0,0,90,
        85,1,0,0,0,90,86,1,0,0,0,90,89,1,0,0,0,91,11,1,0,0,0,92,95,3,42,
        21,0,93,94,5,29,0,0,94,96,3,40,20,0,95,93,1,0,0,0,95,96,1,0,0,0,
        96,97,1,0,0,0,97,100,5,21,0,0,98,101,3,12,6,0,99,101,3,46,23,0,100,
        98,1,0,0,0,100,99,1,0,0,0,101,13,1,0,0,0,102,103,5,33,0,0,103,108,
        3,30,15,0,104,105,5,35,0,0,105,107,3,30,15,0,106,104,1,0,0,0,107,
        110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,114,1,0,0,0,110,
        108,1,0,0,0,111,112,5,34,0,0,112,113,5,29,0,0,113,115,3,32,16,0,
        114,111,1,0,0,0,114,115,1,0,0,0,115,15,1,0,0,0,116,117,5,36,0,0,
        117,118,3,46,23,0,118,119,5,29,0,0,119,120,3,32,16,0,120,17,1,0,
        0,0,121,122,5,38,0,0,122,123,5,46,0,0,123,124,5,39,0,0,124,125,3,
        46,23,0,125,126,5,29,0,0,126,127,3,32,16,0,127,19,1,0,0,0,128,129,
        5,37,0,0,129,130,5,22,0,0,130,131,3,46,23,0,131,132,5,23,0,0,132,
        21,1,0,0,0,133,134,5,40,0,0,134,135,5,46,0,0,135,152,5,22,0,0,136,
        139,3,44,22,0,137,138,5,29,0,0,138,140,3,40,20,0,139,137,1,0,0,0,
        139,140,1,0,0,0,140,149,1,0,0,0,141,142,5,28,0,0,142,145,3,44,22,
        0,143,144,5,29,0,0,144,146,3,40,20,0,145,143,1,0,0,0,145,146,1,0,
        0,0,146,148,1,0,0,0,147,141,1,0,0,0,148,151,1,0,0,0,149,147,1,0,
        0,0,149,150,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,152,136,1,0,
        0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,158,5,23,0,0,155,156,5,14,
        0,0,156,157,5,9,0,0,157,159,3,40,20,0,158,155,1,0,0,0,158,159,1,
        0,0,0,159,160,1,0,0,0,160,163,5,29,0,0,161,164,5,52,0,0,162,164,
        3,6,3,0,163,161,1,0,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,163,
        1,0,0,0,165,166,1,0,0,0,166,23,1,0,0,0,167,168,5,42,0,0,168,173,
        5,46,0,0,169,170,5,45,0,0,170,172,5,46,0,0,171,169,1,0,0,0,172,175,
        1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,181,1,0,0,0,175,173,
        1,0,0,0,176,177,5,43,0,0,177,178,5,46,0,0,178,179,5,42,0,0,179,181,
        5,46,0,0,180,167,1,0,0,0,180,176,1,0,0,0,181,25,1,0,0,0,182,186,
        3,42,21,0,183,186,5,20,0,0,184,186,5,46,0,0,185,182,1,0,0,0,185,
        183,1,0,0,0,185,184,1,0,0,0,186,187,1,0,0,0,187,208,5,22,0,0,188,
        194,5,47,0,0,189,194,5,48,0,0,190,194,5,49,0,0,191,194,3,42,21,0,
        192,194,3,46,23,0,193,188,1,0,0,0,193,189,1,0,0,0,193,190,1,0,0,
        0,193,191,1,0,0,0,193,192,1,0,0,0,194,205,1,0,0,0,195,201,5,28,0,
        0,196,202,5,47,0,0,197,202,5,48,0,0,198,202,5,49,0,0,199,202,3,42,
        21,0,200,202,3,46,23,0,201,196,1,0,0,0,201,197,1,0,0,0,201,198,1,
        0,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,204,1,0,0,0,203,195,1,
        0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,
        0,0,0,207,205,1,0,0,0,208,193,1,0,0,0,208,209,1,0,0,0,209,238,1,
        0,0,0,210,211,5,46,0,0,211,213,5,21,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,219,1,0,0,0,214,220,5,47,0,0,215,220,5,48,0,0,216,220,
        5,49,0,0,217,220,3,42,21,0,218,220,3,46,23,0,219,214,1,0,0,0,219,
        215,1,0,0,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,220,
        235,1,0,0,0,221,224,5,28,0,0,222,223,5,46,0,0,223,225,5,21,0,0,224,
        222,1,0,0,0,224,225,1,0,0,0,225,231,1,0,0,0,226,232,5,47,0,0,227,
        232,5,48,0,0,228,232,5,49,0,0,229,232,3,42,21,0,230,232,3,46,23,
        0,231,226,1,0,0,0,231,227,1,0,0,0,231,228,1,0,0,0,231,229,1,0,0,
        0,231,230,1,0,0,0,232,234,1,0,0,0,233,221,1,0,0,0,234,237,1,0,0,
        0,235,233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,
        0,238,212,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,241,5,23,0,
        0,241,27,1,0,0,0,242,244,5,41,0,0,243,245,5,22,0,0,244,243,1,0,0,
        0,244,245,1,0,0,0,245,246,1,0,0,0,246,248,3,46,23,0,247,249,5,23,
        0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,251,5,52,
        0,0,251,29,1,0,0,0,252,253,3,46,23,0,253,255,5,29,0,0,254,256,5,
        52,0,0,255,254,1,0,0,0,255,256,1,0,0,0,256,257,1,0,0,0,257,258,3,
        32,16,0,258,31,1,0,0,0,259,262,3,6,3,0,260,262,5,52,0,0,261,259,
        1,0,0,0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,
        1,0,0,0,264,270,1,0,0,0,265,263,1,0,0,0,266,267,3,6,3,0,267,268,
        5,52,0,0,268,270,1,0,0,0,269,263,1,0,0,0,269,266,1,0,0,0,270,33,
        1,0,0,0,271,280,5,26,0,0,272,277,3,46,23,0,273,274,5,28,0,0,274,
        276,3,46,23,0,275,273,1,0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,
        278,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,280,272,1,0,0,0,280,
        281,1,0,0,0,281,282,1,0,0,0,282,295,5,27,0,0,283,284,5,26,0,0,284,
        285,3,46,23,0,285,289,5,29,0,0,286,287,3,46,23,0,287,288,5,29,0,
        0,288,290,1,0,0,0,289,286,1,0,0,0,289,290,1,0,0,0,290,291,1,0,0,
        0,291,292,3,46,23,0,292,293,5,27,0,0,293,295,1,0,0,0,294,271,1,0,
        0,0,294,283,1,0,0,0,295,35,1,0,0,0,296,305,5,22,0,0,297,302,3,46,
        23,0,298,299,5,28,0,0,299,301,3,46,23,0,300,298,1,0,0,0,301,304,
        1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,306,1,0,0,0,304,302,
        1,0,0,0,305,297,1,0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,320,
        5,23,0,0,308,309,5,22,0,0,309,310,3,46,23,0,310,314,5,29,0,0,311,
        312,3,46,23,0,312,313,5,29,0,0,313,315,1,0,0,0,314,311,1,0,0,0,314,
        315,1,0,0,0,315,316,1,0,0,0,316,317,3,46,23,0,317,318,5,23,0,0,318,
        320,1,0,0,0,319,296,1,0,0,0,319,308,1,0,0,0,320,37,1,0,0,0,321,322,
        3,42,21,0,322,323,5,26,0,0,323,324,3,46,23,0,324,325,5,27,0,0,325,
        39,1,0,0,0,326,379,5,20,0,0,327,336,5,26,0,0,328,333,5,20,0,0,329,
        330,5,28,0,0,330,332,5,20,0,0,331,329,1,0,0,0,332,335,1,0,0,0,333,
        331,1,0,0,0,333,334,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,336,
        328,1,0,0,0,336,337,1,0,0,0,337,338,1,0,0,0,338,379,5,27,0,0,339,
        340,5,1,0,0,340,349,5,26,0,0,341,346,5,20,0,0,342,343,5,28,0,0,343,
        345,5,20,0,0,344,342,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,
        347,1,0,0,0,347,350,1,0,0,0,348,346,1,0,0,0,349,341,1,0,0,0,349,
        350,1,0,0,0,350,351,1,0,0,0,351,379,5,27,0,0,352,353,5,2,0,0,353,
        362,5,26,0,0,354,359,5,20,0,0,355,356,5,28,0,0,356,358,5,20,0,0,
        357,355,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,359,360,1,0,0,0,
        360,363,1,0,0,0,361,359,1,0,0,0,362,354,1,0,0,0,362,363,1,0,0,0,
        363,364,1,0,0,0,364,379,5,27,0,0,365,366,5,3,0,0,366,375,5,26,0,
        0,367,372,5,20,0,0,368,369,5,28,0,0,369,371,5,20,0,0,370,368,1,0,
        0,0,371,374,1,0,0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,376,1,0,
        0,0,374,372,1,0,0,0,375,367,1,0,0,0,375,376,1,0,0,0,376,377,1,0,
        0,0,377,379,5,27,0,0,378,326,1,0,0,0,378,327,1,0,0,0,378,339,1,0,
        0,0,378,352,1,0,0,0,378,365,1,0,0,0,379,41,1,0,0,0,380,385,5,46,
        0,0,381,382,5,45,0,0,382,384,5,46,0,0,383,381,1,0,0,0,384,387,1,
        0,0,0,385,383,1,0,0,0,385,386,1,0,0,0,386,400,1,0,0,0,387,385,1,
        0,0,0,388,397,5,22,0,0,389,394,3,46,23,0,390,391,5,28,0,0,391,393,
        3,46,23,0,392,390,1,0,0,0,393,396,1,0,0,0,394,392,1,0,0,0,394,395,
        1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,397,389,1,0,0,0,397,398,
        1,0,0,0,398,399,1,0,0,0,399,401,5,23,0,0,400,388,1,0,0,0,400,401,
        1,0,0,0,401,415,1,0,0,0,402,407,5,46,0,0,403,404,5,45,0,0,404,406,
        5,46,0,0,405,403,1,0,0,0,406,409,1,0,0,0,407,405,1,0,0,0,407,408,
        1,0,0,0,408,410,1,0,0,0,409,407,1,0,0,0,410,411,5,26,0,0,411,412,
        3,46,23,0,412,413,5,27,0,0,413,415,1,0,0,0,414,380,1,0,0,0,414,402,
        1,0,0,0,415,43,1,0,0,0,416,419,5,46,0,0,417,418,5,21,0,0,418,420,
        3,46,23,0,419,417,1,0,0,0,419,420,1,0,0,0,420,45,1,0,0,0,421,422,
        6,23,-1,0,422,423,5,14,0,0,423,432,3,46,23,10,424,425,5,19,0,0,425,
        432,3,46,23,9,426,427,5,22,0,0,427,428,3,46,23,0,428,429,5,23,0,
        0,429,432,1,0,0,0,430,432,3,48,24,0,431,421,1,0,0,0,431,424,1,0,
        0,0,431,426,1,0,0,0,431,430,1,0,0,0,432,456,1,0,0,0,433,434,10,11,
        0,0,434,435,5,18,0,0,435,455,3,46,23,11,436,437,10,8,0,0,437,438,
        7,0,0,0,438,455,3,46,23,9,439,440,10,7,0,0,440,441,7,1,0,0,441,455,
        3,46,23,8,442,443,10,6,0,0,443,444,7,2,0,0,444,455,3,46,23,7,445,
        446,10,5,0,0,446,447,7,3,0,0,447,455,3,46,23,6,448,449,10,4,0,0,
        449,450,5,6,0,0,450,455,3,46,23,5,451,452,10,3,0,0,452,453,5,5,0,
        0,453,455,3,46,23,4,454,433,1,0,0,0,454,436,1,0,0,0,454,439,1,0,
        0,0,454,442,1,0,0,0,454,445,1,0,0,0,454,448,1,0,0,0,454,451,1,0,
        0,0,455,458,1,0,0,0,456,454,1,0,0,0,456,457,1,0,0,0,457,47,1,0,0,
        0,458,456,1,0,0,0,459,471,3,26,13,0,460,471,7,4,0,0,461,471,5,49,
        0,0,462,471,3,34,17,0,463,471,3,36,18,0,464,471,3,52,26,0,465,471,
        3,38,19,0,466,471,3,42,21,0,467,471,5,32,0,0,468,471,7,5,0,0,469,
        471,3,50,25,0,470,459,1,0,0,0,470,460,1,0,0,0,470,461,1,0,0,0,470,
        462,1,0,0,0,470,463,1,0,0,0,470,464,1,0,0,0,470,465,1,0,0,0,470,
        466,1,0,0,0,470,467,1,0,0,0,470,468,1,0,0,0,470,469,1,0,0,0,471,
        49,1,0,0,0,472,477,3,42,21,0,473,474,5,28,0,0,474,476,3,42,21,0,
        475,473,1,0,0,0,476,479,1,0,0,0,477,475,1,0,0,0,477,478,1,0,0,0,
        478,481,1,0,0,0,479,477,1,0,0,0,480,472,1,0,0,0,480,481,1,0,0,0,
        481,482,1,0,0,0,482,483,5,21,0,0,483,492,5,4,0,0,484,489,3,42,21,
        0,485,486,5,28,0,0,486,488,3,42,21,0,487,485,1,0,0,0,488,491,1,0,
        0,0,489,487,1,0,0,0,489,490,1,0,0,0,490,493,1,0,0,0,491,489,1,0,
        0,0,492,484,1,0,0,0,492,493,1,0,0,0,493,494,1,0,0,0,494,495,5,29,
        0,0,495,496,3,46,23,0,496,51,1,0,0,0,497,506,5,24,0,0,498,503,3,
        54,27,0,499,500,5,28,0,0,500,502,3,54,27,0,501,499,1,0,0,0,502,505,
        1,0,0,0,503,501,1,0,0,0,503,504,1,0,0,0,504,507,1,0,0,0,505,503,
        1,0,0,0,506,498,1,0,0,0,506,507,1,0,0,0,507,508,1,0,0,0,508,545,
        5,25,0,0,509,518,5,24,0,0,510,515,7,6,0,0,511,512,5,28,0,0,512,514,
        7,6,0,0,513,511,1,0,0,0,514,517,1,0,0,0,515,513,1,0,0,0,515,516,
        1,0,0,0,516,519,1,0,0,0,517,515,1,0,0,0,518,510,1,0,0,0,518,519,
        1,0,0,0,519,520,1,0,0,0,520,545,5,25,0,0,521,530,5,24,0,0,522,527,
        3,46,23,0,523,524,5,28,0,0,524,526,3,46,23,0,525,523,1,0,0,0,526,
        529,1,0,0,0,527,525,1,0,0,0,527,528,1,0,0,0,528,531,1,0,0,0,529,
        527,1,0,0,0,530,522,1,0,0,0,530,531,1,0,0,0,531,532,1,0,0,0,532,
        545,5,25,0,0,533,534,5,24,0,0,534,535,3,46,23,0,535,539,5,29,0,0,
        536,537,3,46,23,0,537,538,5,29,0,0,538,540,1,0,0,0,539,536,1,0,0,
        0,539,540,1,0,0,0,540,541,1,0,0,0,541,542,3,46,23,0,542,543,5,25,
        0,0,543,545,1,0,0,0,544,497,1,0,0,0,544,509,1,0,0,0,544,521,1,0,
        0,0,544,533,1,0,0,0,545,53,1,0,0,0,546,547,5,46,0,0,547,548,5,29,
        0,0,548,556,3,46,23,0,549,550,5,49,0,0,550,551,5,29,0,0,551,556,
        3,46,23,0,552,553,5,47,0,0,553,554,5,29,0,0,554,556,3,46,23,0,555,
        546,1,0,0,0,555,549,1,0,0,0,555,552,1,0,0,0,556,55,1,0,0,0,77,58,
        65,67,74,80,90,95,100,108,114,139,145,149,152,158,163,165,173,180,
        185,193,201,205,208,212,219,224,231,235,238,244,248,255,261,263,
        269,277,280,289,294,302,305,314,319,333,336,346,349,359,362,372,
        375,378,385,394,397,400,407,414,419,431,454,456,470,477,480,489,
        492,503,506,515,518,527,530,539,544,555
    ]

class python_grammarParser ( Parser ):

    grammarFileName = "python_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dict'", "'list'", "'tuple'", "'lambda'", 
                     "'or'", "'and'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "<INVALID>", "'%'", "'**'", 
                     "'not'", "<INVALID>", "'='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "':'", "'True'", "'False'", "'None'", 
                     "'if'", "'else'", "'elif'", "'while'", "'print'", "'for'", 
                     "'in'", "'def'", "'return'", "'import'", "'from'", 
                     "'todo'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LAMBDA", "OR", "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", 
                      "LTEQ", "PLUS", "MINUS", "MULT", "DIV", "MOD", "POW", 
                      "NOT", "TYPES", "ASSIGN", "OPAR", "CPAR", "OBRACE", 
                      "CBRACE", "OKEY", "CKEY", "COMMA", "POINTS", "TRUE", 
                      "FALSE", "NULL", "IF", "ELSE", "ELIF", "WHILE", "LOG", 
                      "FOR", "IN", "FUNCION", "RETORNO", "IMPORT", "FROM", 
                      "ASTERISC", "POINT", "ID", "INT", "FLOAT", "STRING", 
                      "COMMENT", "SPACE", "NEWLINE", "OTHER" ]

    RULE_parse = 0
    RULE_from_input = 1
    RULE_from_file = 2
    RULE_stat = 3
    RULE_compound_stat = 4
    RULE_simple_stat = 5
    RULE_assignment = 6
    RULE_if_stat = 7
    RULE_while_stat = 8
    RULE_for_stat = 9
    RULE_log = 10
    RULE_funcion = 11
    RULE_importar = 12
    RULE_call_function = 13
    RULE_retornar = 14
    RULE_condition_block = 15
    RULE_stat_block = 16
    RULE_array = 17
    RULE_tuple = 18
    RULE_accessarray = 19
    RULE_type_anotation = 20
    RULE_variable = 21
    RULE_parametro = 22
    RULE_expr = 23
    RULE_atom = 24
    RULE_lambda_func = 25
    RULE_objeto = 26
    RULE_keyvalue = 27

    ruleNames =  [ "parse", "from_input", "from_file", "stat", "compound_stat", 
                   "simple_stat", "assignment", "if_stat", "while_stat", 
                   "for_stat", "log", "funcion", "importar", "call_function", 
                   "retornar", "condition_block", "stat_block", "array", 
                   "tuple", "accessarray", "type_anotation", "variable", 
                   "parametro", "expr", "atom", "lambda_func", "objeto", 
                   "keyvalue" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LAMBDA=4
    OR=5
    AND=6
    EQ=7
    NEQ=8
    GT=9
    LT=10
    GTEQ=11
    LTEQ=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    MOD=17
    POW=18
    NOT=19
    TYPES=20
    ASSIGN=21
    OPAR=22
    CPAR=23
    OBRACE=24
    CBRACE=25
    OKEY=26
    CKEY=27
    COMMA=28
    POINTS=29
    TRUE=30
    FALSE=31
    NULL=32
    IF=33
    ELSE=34
    ELIF=35
    WHILE=36
    LOG=37
    FOR=38
    IN=39
    FUNCION=40
    RETORNO=41
    IMPORT=42
    FROM=43
    ASTERISC=44
    POINT=45
    ID=46
    INT=47
    FLOAT=48
    STRING=49
    COMMENT=50
    SPACE=51
    NEWLINE=52
    OTHER=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_input(self):
            return self.getTypedRuleContext(python_grammarParser.From_inputContext,0)


        def from_file(self):
            return self.getTypedRuleContext(python_grammarParser.From_fileContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = python_grammarParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.from_input()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.from_file()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(python_grammarParser.StatContext,0)


        def NEWLINE(self):
            return self.getToken(python_grammarParser.NEWLINE, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_from_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_input" ):
                listener.enterFrom_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_input" ):
                listener.exitFrom_input(self)




    def from_input(self):

        localctx = python_grammarParser.From_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_from_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.stat()
            self.state = 61
            self.match(python_grammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(python_grammarParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.StatContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.NEWLINE)
            else:
                return self.getToken(python_grammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_from_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_file" ):
                listener.enterFrom_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_file" ):
                listener.exitFrom_file(self)




    def from_file(self):

        localctx = python_grammarParser.From_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_from_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 14583319952883712) != 0:
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20, 21, 22, 24, 26, 30, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 46, 47, 48, 49, 53]:
                    self.state = 63
                    self.stat()
                    pass
                elif token in [52]:
                    self.state = 64
                    self.match(python_grammarParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(python_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stat(self):
            return self.getTypedRuleContext(python_grammarParser.Simple_statContext,0)


        def compound_stat(self):
            return self.getTypedRuleContext(python_grammarParser.Compound_statContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = python_grammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 24, 26, 30, 31, 32, 37, 41, 42, 43, 46, 47, 48, 49, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.simple_stat()
                pass
            elif token in [33, 36, 38, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.compound_stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stat(self):
            return self.getTypedRuleContext(python_grammarParser.If_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(python_grammarParser.While_statContext,0)


        def for_stat(self):
            return self.getTypedRuleContext(python_grammarParser.For_statContext,0)


        def funcion(self):
            return self.getTypedRuleContext(python_grammarParser.FuncionContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_compound_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stat" ):
                listener.enterCompound_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stat" ):
                listener.exitCompound_stat(self)




    def compound_stat(self):

        localctx = python_grammarParser.Compound_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compound_stat)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.if_stat()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.while_stat()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.for_stat()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.funcion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(python_grammarParser.AssignmentContext,0)


        def log(self):
            return self.getTypedRuleContext(python_grammarParser.LogContext,0)


        def importar(self):
            return self.getTypedRuleContext(python_grammarParser.ImportarContext,0)


        def retornar(self):
            return self.getTypedRuleContext(python_grammarParser.RetornarContext,0)


        def atom(self):
            return self.getTypedRuleContext(python_grammarParser.AtomContext,0)


        def NEWLINE(self):
            return self.getToken(python_grammarParser.NEWLINE, 0)

        def OTHER(self):
            return self.getToken(python_grammarParser.OTHER, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_simple_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stat" ):
                listener.enterSimple_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stat" ):
                listener.exitSimple_stat(self)




    def simple_stat(self):

        localctx = python_grammarParser.Simple_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_simple_stat)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.log()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.importar()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.retornar()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.atom()
                self.state = 87
                self.match(python_grammarParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.match(python_grammarParser.OTHER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(python_grammarParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(python_grammarParser.ASSIGN, 0)

        def assignment(self):
            return self.getTypedRuleContext(python_grammarParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def type_anotation(self):
            return self.getTypedRuleContext(python_grammarParser.Type_anotationContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = python_grammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.variable()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 93
                self.match(python_grammarParser.POINTS)
                self.state = 94
                self.type_anotation()


            self.state = 97
            self.match(python_grammarParser.ASSIGN)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 98
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 99
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(python_grammarParser.IF, 0)

        def condition_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.Condition_blockContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.Condition_blockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ELIF)
            else:
                return self.getToken(python_grammarParser.ELIF, i)

        def ELSE(self):
            return self.getToken(python_grammarParser.ELSE, 0)

        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def stat_block(self):
            return self.getTypedRuleContext(python_grammarParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)




    def if_stat(self):

        localctx = python_grammarParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(python_grammarParser.IF)
            self.state = 103
            self.condition_block()
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.match(python_grammarParser.ELIF)
                    self.state = 105
                    self.condition_block() 
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(python_grammarParser.ELSE)
                self.state = 112
                self.match(python_grammarParser.POINTS)
                self.state = 113
                self.stat_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(python_grammarParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def stat_block(self):
            return self.getTypedRuleContext(python_grammarParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)




    def while_stat(self):

        localctx = python_grammarParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(python_grammarParser.WHILE)
            self.state = 117
            self.expr(0)
            self.state = 118
            self.match(python_grammarParser.POINTS)
            self.state = 119
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(python_grammarParser.FOR, 0)

        def ID(self):
            return self.getToken(python_grammarParser.ID, 0)

        def IN(self):
            return self.getToken(python_grammarParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def stat_block(self):
            return self.getTypedRuleContext(python_grammarParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_for_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stat" ):
                listener.enterFor_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stat" ):
                listener.exitFor_stat(self)




    def for_stat(self):

        localctx = python_grammarParser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(python_grammarParser.FOR)
            self.state = 122
            self.match(python_grammarParser.ID)
            self.state = 123
            self.match(python_grammarParser.IN)
            self.state = 124
            self.expr(0)
            self.state = 125
            self.match(python_grammarParser.POINTS)
            self.state = 126
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(python_grammarParser.LOG, 0)

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)




    def log(self):

        localctx = python_grammarParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(python_grammarParser.LOG)
            self.state = 129
            self.match(python_grammarParser.OPAR)
            self.state = 130
            self.expr(0)
            self.state = 131
            self.match(python_grammarParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(python_grammarParser.FUNCION, 0)

        def ID(self):
            return self.getToken(python_grammarParser.ID, 0)

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def POINTS(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINTS)
            else:
                return self.getToken(python_grammarParser.POINTS, i)

        def MINUS(self):
            return self.getToken(python_grammarParser.MINUS, 0)

        def GT(self):
            return self.getToken(python_grammarParser.GT, 0)

        def type_anotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.Type_anotationContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.Type_anotationContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.NEWLINE)
            else:
                return self.getToken(python_grammarParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.StatContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.StatContext,i)


        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ParametroContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ParametroContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = python_grammarParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(python_grammarParser.FUNCION)
            self.state = 134
            self.match(python_grammarParser.ID)
            self.state = 135
            self.match(python_grammarParser.OPAR)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 136
                self.parametro()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 137
                    self.match(python_grammarParser.POINTS)
                    self.state = 138
                    self.type_anotation()


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 141
                    self.match(python_grammarParser.COMMA)

                    self.state = 142
                    self.parametro()
                    self.state = 145
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==29:
                        self.state = 143
                        self.match(python_grammarParser.POINTS)
                        self.state = 144
                        self.type_anotation()


                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 154
            self.match(python_grammarParser.CPAR)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 155
                self.match(python_grammarParser.MINUS)
                self.state = 156
                self.match(python_grammarParser.GT)
                self.state = 157
                self.type_anotation()


            self.state = 160
            self.match(python_grammarParser.POINTS)
            self.state = 163 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 163
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [52]:
                        self.state = 161
                        self.match(python_grammarParser.NEWLINE)
                        pass
                    elif token in [20, 21, 22, 24, 26, 30, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 46, 47, 48, 49, 53]:
                        self.state = 162
                        self.stat()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 165 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(python_grammarParser.IMPORT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ID)
            else:
                return self.getToken(python_grammarParser.ID, i)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINT)
            else:
                return self.getToken(python_grammarParser.POINT, i)

        def FROM(self):
            return self.getToken(python_grammarParser.FROM, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_importar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportar" ):
                listener.enterImportar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportar" ):
                listener.exitImportar(self)




    def importar(self):

        localctx = python_grammarParser.ImportarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_importar)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(python_grammarParser.IMPORT)
                self.state = 168
                self.match(python_grammarParser.ID)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 169
                    self.match(python_grammarParser.POINT)
                    self.state = 170
                    self.match(python_grammarParser.ID)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(python_grammarParser.FROM)
                self.state = 177
                self.match(python_grammarParser.ID)
                self.state = 178
                self.match(python_grammarParser.IMPORT)
                self.state = 179
                self.match(python_grammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.VariableContext,i)


        def TYPES(self):
            return self.getToken(python_grammarParser.TYPES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ID)
            else:
                return self.getToken(python_grammarParser.ID, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.INT)
            else:
                return self.getToken(python_grammarParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.FLOAT)
            else:
                return self.getToken(python_grammarParser.FLOAT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.STRING)
            else:
                return self.getToken(python_grammarParser.STRING, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ASSIGN)
            else:
                return self.getToken(python_grammarParser.ASSIGN, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_call_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_function" ):
                listener.enterCall_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_function" ):
                listener.exitCall_function(self)




    def call_function(self):

        localctx = python_grammarParser.Call_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 182
                self.variable()
                pass

            elif la_ == 2:
                self.state = 183
                self.match(python_grammarParser.TYPES)
                pass

            elif la_ == 3:
                self.state = 184
                self.match(python_grammarParser.ID)
                pass


            self.state = 187
            self.match(python_grammarParser.OPAR)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 193
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 188
                    self.match(python_grammarParser.INT)
                    pass

                elif la_ == 2:
                    self.state = 189
                    self.match(python_grammarParser.FLOAT)
                    pass

                elif la_ == 3:
                    self.state = 190
                    self.match(python_grammarParser.STRING)
                    pass

                elif la_ == 4:
                    self.state = 191
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 192
                    self.expr(0)
                    pass


                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 195
                    self.match(python_grammarParser.COMMA)
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        self.state = 196
                        self.match(python_grammarParser.INT)
                        pass

                    elif la_ == 2:
                        self.state = 197
                        self.match(python_grammarParser.FLOAT)
                        pass

                    elif la_ == 3:
                        self.state = 198
                        self.match(python_grammarParser.STRING)
                        pass

                    elif la_ == 4:
                        self.state = 199
                        self.variable()
                        pass

                    elif la_ == 5:
                        self.state = 200
                        self.expr(0)
                        pass


                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1055538770624512) != 0:
                self.state = 212
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 210
                    self.match(python_grammarParser.ID)
                    self.state = 211
                    self.match(python_grammarParser.ASSIGN)


                self.state = 219
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 214
                    self.match(python_grammarParser.INT)
                    pass

                elif la_ == 2:
                    self.state = 215
                    self.match(python_grammarParser.FLOAT)
                    pass

                elif la_ == 3:
                    self.state = 216
                    self.match(python_grammarParser.STRING)
                    pass

                elif la_ == 4:
                    self.state = 217
                    self.variable()
                    pass

                elif la_ == 5:
                    self.state = 218
                    self.expr(0)
                    pass


                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 221
                    self.match(python_grammarParser.COMMA)

                    self.state = 224
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        self.state = 222
                        self.match(python_grammarParser.ID)
                        self.state = 223
                        self.match(python_grammarParser.ASSIGN)


                    self.state = 231
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 226
                        self.match(python_grammarParser.INT)
                        pass

                    elif la_ == 2:
                        self.state = 227
                        self.match(python_grammarParser.FLOAT)
                        pass

                    elif la_ == 3:
                        self.state = 228
                        self.match(python_grammarParser.STRING)
                        pass

                    elif la_ == 4:
                        self.state = 229
                        self.variable()
                        pass

                    elif la_ == 5:
                        self.state = 230
                        self.expr(0)
                        pass


                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 240
            self.match(python_grammarParser.CPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNO(self):
            return self.getToken(python_grammarParser.RETORNO, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(python_grammarParser.NEWLINE, 0)

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_retornar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetornar" ):
                listener.enterRetornar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetornar" ):
                listener.exitRetornar(self)




    def retornar(self):

        localctx = python_grammarParser.RetornarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_retornar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(python_grammarParser.RETORNO)
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 243
                self.match(python_grammarParser.OPAR)


            self.state = 246
            self.expr(0)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 247
                self.match(python_grammarParser.CPAR)


            self.state = 250
            self.match(python_grammarParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def stat_block(self):
            return self.getTypedRuleContext(python_grammarParser.Stat_blockContext,0)


        def NEWLINE(self):
            return self.getToken(python_grammarParser.NEWLINE, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_condition_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_block" ):
                listener.enterCondition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_block" ):
                listener.exitCondition_block(self)




    def condition_block(self):

        localctx = python_grammarParser.Condition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expr(0)
            self.state = 253
            self.match(python_grammarParser.POINTS)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(python_grammarParser.NEWLINE)


            self.state = 257
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.StatContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.StatContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.NEWLINE)
            else:
                return self.getToken(python_grammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_stat_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_block" ):
                listener.enterStat_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_block" ):
                listener.exitStat_block(self)




    def stat_block(self):

        localctx = python_grammarParser.Stat_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stat_block)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 261
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [20, 21, 22, 24, 26, 30, 31, 32, 33, 36, 37, 38, 40, 41, 42, 43, 46, 47, 48, 49, 53]:
                            self.state = 259
                            self.stat()
                            pass
                        elif token in [52]:
                            self.state = 260
                            self.match(python_grammarParser.NEWLINE)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 265
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.stat()
                self.state = 267
                self.match(python_grammarParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start = None # ExprContext
            self.step = None # ExprContext
            self.end = None # ExprContext

        def OKEY(self):
            return self.getToken(python_grammarParser.OKEY, 0)

        def CKEY(self):
            return self.getToken(python_grammarParser.CKEY, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def POINTS(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINTS)
            else:
                return self.getToken(python_grammarParser.POINTS, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = python_grammarParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(python_grammarParser.OKEY)
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1055538770624512) != 0:
                    self.state = 272
                    self.expr(0)
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 273
                        self.match(python_grammarParser.COMMA)
                        self.state = 274
                        self.expr(0)
                        self.state = 279
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 282
                self.match(python_grammarParser.CKEY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.match(python_grammarParser.OKEY)
                self.state = 284
                localctx.start = self.expr(0)
                self.state = 285
                self.match(python_grammarParser.POINTS)
                self.state = 289
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 286
                    localctx.step = self.expr(0)
                    self.state = 287
                    self.match(python_grammarParser.POINTS)


                self.state = 291
                localctx.end = self.expr(0)
                self.state = 292
                self.match(python_grammarParser.CKEY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start = None # ExprContext
            self.step = None # ExprContext
            self.end = None # ExprContext

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def POINTS(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINTS)
            else:
                return self.getToken(python_grammarParser.POINTS, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)




    def tuple_(self):

        localctx = python_grammarParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(python_grammarParser.OPAR)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1055538770624512) != 0:
                    self.state = 297
                    self.expr(0)
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 298
                        self.match(python_grammarParser.COMMA)
                        self.state = 299
                        self.expr(0)
                        self.state = 304
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 307
                self.match(python_grammarParser.CPAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(python_grammarParser.OPAR)
                self.state = 309
                localctx.start = self.expr(0)
                self.state = 310
                self.match(python_grammarParser.POINTS)
                self.state = 314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 311
                    localctx.step = self.expr(0)
                    self.state = 312
                    self.match(python_grammarParser.POINTS)


                self.state = 316
                localctx.end = self.expr(0)
                self.state = 317
                self.match(python_grammarParser.CPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessarrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(python_grammarParser.VariableContext,0)


        def OKEY(self):
            return self.getToken(python_grammarParser.OKEY, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def CKEY(self):
            return self.getToken(python_grammarParser.CKEY, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_accessarray

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessarray" ):
                listener.enterAccessarray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessarray" ):
                listener.exitAccessarray(self)




    def accessarray(self):

        localctx = python_grammarParser.AccessarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_accessarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.variable()
            self.state = 322
            self.match(python_grammarParser.OKEY)
            self.state = 323
            self.expr(0)
            self.state = 324
            self.match(python_grammarParser.CKEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_anotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPES(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.TYPES)
            else:
                return self.getToken(python_grammarParser.TYPES, i)

        def OKEY(self):
            return self.getToken(python_grammarParser.OKEY, 0)

        def CKEY(self):
            return self.getToken(python_grammarParser.CKEY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_type_anotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_anotation" ):
                listener.enterType_anotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_anotation" ):
                listener.exitType_anotation(self)




    def type_anotation(self):

        localctx = python_grammarParser.Type_anotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_type_anotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 326
                self.match(python_grammarParser.TYPES)
                pass
            elif token in [26]:
                self.state = 327
                self.match(python_grammarParser.OKEY)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 328
                    self.match(python_grammarParser.TYPES)
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 329
                        self.match(python_grammarParser.COMMA)
                        self.state = 330
                        self.match(python_grammarParser.TYPES)
                        self.state = 335
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 338
                self.match(python_grammarParser.CKEY)
                pass
            elif token in [1]:
                self.state = 339
                self.match(python_grammarParser.T__0)
                self.state = 340
                self.match(python_grammarParser.OKEY)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 341
                    self.match(python_grammarParser.TYPES)
                    self.state = 346
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 342
                        self.match(python_grammarParser.COMMA)
                        self.state = 343
                        self.match(python_grammarParser.TYPES)
                        self.state = 348
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 351
                self.match(python_grammarParser.CKEY)
                pass
            elif token in [2]:
                self.state = 352
                self.match(python_grammarParser.T__1)
                self.state = 353
                self.match(python_grammarParser.OKEY)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 354
                    self.match(python_grammarParser.TYPES)
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 355
                        self.match(python_grammarParser.COMMA)
                        self.state = 356
                        self.match(python_grammarParser.TYPES)
                        self.state = 361
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 364
                self.match(python_grammarParser.CKEY)
                pass
            elif token in [3]:
                self.state = 365
                self.match(python_grammarParser.T__2)
                self.state = 366
                self.match(python_grammarParser.OKEY)
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 367
                    self.match(python_grammarParser.TYPES)
                    self.state = 372
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 368
                        self.match(python_grammarParser.COMMA)
                        self.state = 369
                        self.match(python_grammarParser.TYPES)
                        self.state = 374
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 377
                self.match(python_grammarParser.CKEY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ID)
            else:
                return self.getToken(python_grammarParser.ID, i)

        def POINT(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINT)
            else:
                return self.getToken(python_grammarParser.POINT, i)

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def OKEY(self):
            return self.getToken(python_grammarParser.OKEY, 0)

        def CKEY(self):
            return self.getToken(python_grammarParser.CKEY, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = python_grammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(python_grammarParser.ID)
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 381
                        self.match(python_grammarParser.POINT)
                        self.state = 382
                        self.match(python_grammarParser.ID) 
                    self.state = 387
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 400
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 388
                    self.match(python_grammarParser.OPAR)
                    self.state = 397
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1055538770624512) != 0:
                        self.state = 389
                        self.expr(0)
                        self.state = 394
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==28:
                            self.state = 390
                            self.match(python_grammarParser.COMMA)
                            self.state = 391
                            self.expr(0)
                            self.state = 396
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 399
                    self.match(python_grammarParser.CPAR)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(python_grammarParser.ID)
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 403
                    self.match(python_grammarParser.POINT)
                    self.state = 404
                    self.match(python_grammarParser.ID)
                    self.state = 409
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 410
                self.match(python_grammarParser.OKEY)
                self.state = 411
                self.expr(0)
                self.state = 412
                self.match(python_grammarParser.CKEY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(python_grammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(python_grammarParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def getRuleIndex(self):
            return python_grammarParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = python_grammarParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(python_grammarParser.ID)
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 417
                self.match(python_grammarParser.ASSIGN)
                self.state = 418
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return python_grammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPAR(self):
            return self.getToken(python_grammarParser.OPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)

        def CPAR(self):
            return self.getToken(python_grammarParser.CPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpr" ):
                listener.enterParExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpr" ):
                listener.exitParExpr(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(python_grammarParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(python_grammarParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)

        def MULT(self):
            return self.getToken(python_grammarParser.MULT, 0)
        def DIV(self):
            return self.getToken(python_grammarParser.DIV, 0)
        def MOD(self):
            return self.getToken(python_grammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(python_grammarParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def OR(self):
            return self.getToken(python_grammarParser.OR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(python_grammarParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(python_grammarParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)


    class PowExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(python_grammarParser.POW, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpr" ):
                listener.enterPowExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpr" ):
                listener.exitPowExpr(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)

        def LTEQ(self):
            return self.getToken(python_grammarParser.LTEQ, 0)
        def GTEQ(self):
            return self.getToken(python_grammarParser.GTEQ, 0)
        def LT(self):
            return self.getToken(python_grammarParser.LT, 0)
        def GT(self):
            return self.getToken(python_grammarParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)

        def EQ(self):
            return self.getToken(python_grammarParser.EQ, 0)
        def NEQ(self):
            return self.getToken(python_grammarParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def AND(self):
            return self.getToken(python_grammarParser.AND, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = python_grammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = python_grammarParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 422
                self.match(python_grammarParser.MINUS)
                self.state = 423
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = python_grammarParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 424
                self.match(python_grammarParser.NOT)
                self.state = 425
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = python_grammarParser.ParExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 426
                self.match(python_grammarParser.OPAR)
                self.state = 427
                self.expr(0)
                self.state = 428
                self.match(python_grammarParser.CPAR)
                pass

            elif la_ == 4:
                localctx = python_grammarParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 430
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 454
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        localctx = python_grammarParser.PowExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 433
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 434
                        self.match(python_grammarParser.POW)
                        self.state = 435
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = python_grammarParser.MultiplicationExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 436
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 437
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 438
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = python_grammarParser.AdditiveExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 439
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 440
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 441
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = python_grammarParser.RelationalExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 442
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 443
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 444
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = python_grammarParser.EqualityExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 445
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 446
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 447
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = python_grammarParser.AndExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 448
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 449
                        self.match(python_grammarParser.AND)
                        self.state = 450
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 7:
                        localctx = python_grammarParser.OrExprContext(self, python_grammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 451
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 452
                        self.match(python_grammarParser.OR)
                        self.state = 453
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return python_grammarParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ObjetoAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objeto(self):
            return self.getTypedRuleContext(python_grammarParser.ObjetoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjetoAtom" ):
                listener.enterObjetoAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjetoAtom" ):
                listener.exitObjetoAtom(self)


    class AccessToarrayContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def accessarray(self):
            return self.getTypedRuleContext(python_grammarParser.AccessarrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessToarray" ):
                listener.enterAccessToarray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessToarray" ):
                listener.exitAccessToarray(self)


    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(python_grammarParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(python_grammarParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtom" ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtom" ):
                listener.exitBooleanAtom(self)


    class CallAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call_function(self):
            return self.getTypedRuleContext(python_grammarParser.Call_functionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallAtom" ):
                listener.enterCallAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallAtom" ):
                listener.exitCallAtom(self)


    class ArrayAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(python_grammarParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAtom" ):
                listener.enterArrayAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAtom" ):
                listener.exitArrayAtom(self)


    class NULLAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NULL(self):
            return self.getToken(python_grammarParser.NULL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNULLAtom" ):
                listener.enterNULLAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNULLAtom" ):
                listener.exitNULLAtom(self)


    class StringAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(python_grammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringAtom" ):
                listener.enterStringAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringAtom" ):
                listener.exitStringAtom(self)


    class TupleAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tuple_(self):
            return self.getTypedRuleContext(python_grammarParser.TupleContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupleAtom" ):
                listener.enterTupleAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupleAtom" ):
                listener.exitTupleAtom(self)


    class AccessVariableContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(python_grammarParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessVariable" ):
                listener.enterAccessVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessVariable" ):
                listener.exitAccessVariable(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(python_grammarParser.INT, 0)
        def FLOAT(self):
            return self.getToken(python_grammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)


    class LambdaAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_grammarParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lambda_func(self):
            return self.getTypedRuleContext(python_grammarParser.Lambda_funcContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaAtom" ):
                listener.enterLambdaAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaAtom" ):
                listener.exitLambdaAtom(self)



    def atom(self):

        localctx = python_grammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                localctx = python_grammarParser.CallAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.call_function()
                pass

            elif la_ == 2:
                localctx = python_grammarParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = python_grammarParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.match(python_grammarParser.STRING)
                pass

            elif la_ == 4:
                localctx = python_grammarParser.ArrayAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 462
                self.array()
                pass

            elif la_ == 5:
                localctx = python_grammarParser.TupleAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 463
                self.tuple_()
                pass

            elif la_ == 6:
                localctx = python_grammarParser.ObjetoAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 464
                self.objeto()
                pass

            elif la_ == 7:
                localctx = python_grammarParser.AccessToarrayContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 465
                self.accessarray()
                pass

            elif la_ == 8:
                localctx = python_grammarParser.AccessVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 466
                self.variable()
                pass

            elif la_ == 9:
                localctx = python_grammarParser.NULLAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 467
                self.match(python_grammarParser.NULL)
                pass

            elif la_ == 10:
                localctx = python_grammarParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 468
                _la = self._input.LA(1)
                if not(_la==47 or _la==48):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 11:
                localctx = python_grammarParser.LambdaAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 469
                self.lambda_func()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lambda_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(python_grammarParser.ASSIGN, 0)

        def LAMBDA(self):
            return self.getToken(python_grammarParser.LAMBDA, 0)

        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.VariableContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_lambda_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda_func" ):
                listener.enterLambda_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda_func" ):
                listener.exitLambda_func(self)




    def lambda_func(self):

        localctx = python_grammarParser.Lambda_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_lambda_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 472
                self.variable()
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 473
                    self.match(python_grammarParser.COMMA)
                    self.state = 474
                    self.variable()
                    self.state = 479
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 482
            self.match(python_grammarParser.ASSIGN)
            self.state = 483
            self.match(python_grammarParser.LAMBDA)
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 484
                self.variable()
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 485
                    self.match(python_grammarParser.COMMA)
                    self.state = 486
                    self.variable()
                    self.state = 491
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 494
            self.match(python_grammarParser.POINTS)
            self.state = 495
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.start = None # ExprContext
            self.step = None # ExprContext
            self.end = None # ExprContext

        def OBRACE(self):
            return self.getToken(python_grammarParser.OBRACE, 0)

        def CBRACE(self):
            return self.getToken(python_grammarParser.CBRACE, 0)

        def keyvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.KeyvalueContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.KeyvalueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.COMMA)
            else:
                return self.getToken(python_grammarParser.COMMA, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.ID)
            else:
                return self.getToken(python_grammarParser.ID, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.STRING)
            else:
                return self.getToken(python_grammarParser.STRING, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.INT)
            else:
                return self.getToken(python_grammarParser.INT, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(python_grammarParser.ExprContext,i)


        def POINTS(self, i:int=None):
            if i is None:
                return self.getTokens(python_grammarParser.POINTS)
            else:
                return self.getToken(python_grammarParser.POINTS, i)

        def getRuleIndex(self):
            return python_grammarParser.RULE_objeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjeto" ):
                listener.enterObjeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjeto" ):
                listener.exitObjeto(self)




    def objeto(self):

        localctx = python_grammarParser.ObjetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_objeto)
        self._la = 0 # Token type
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.match(python_grammarParser.OBRACE)
                self.state = 506
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 774056185954304) != 0:
                    self.state = 498
                    self.keyvalue()
                    self.state = 503
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 499
                        self.match(python_grammarParser.COMMA)
                        self.state = 500
                        self.keyvalue()
                        self.state = 505
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 508
                self.match(python_grammarParser.CBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(python_grammarParser.OBRACE)
                self.state = 518
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 774056185954304) != 0:
                    self.state = 510
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 774056185954304) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 515
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 511
                        self.match(python_grammarParser.COMMA)
                        self.state = 512
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 774056185954304) != 0):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 517
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 520
                self.match(python_grammarParser.CBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
                self.match(python_grammarParser.OBRACE)
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 1055538770624512) != 0:
                    self.state = 522
                    self.expr(0)
                    self.state = 527
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==28:
                        self.state = 523
                        self.match(python_grammarParser.COMMA)
                        self.state = 524
                        self.expr(0)
                        self.state = 529
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 532
                self.match(python_grammarParser.CBRACE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.match(python_grammarParser.OBRACE)
                self.state = 534
                localctx.start = self.expr(0)
                self.state = 535
                self.match(python_grammarParser.POINTS)
                self.state = 539
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
                if la_ == 1:
                    self.state = 536
                    localctx.step = self.expr(0)
                    self.state = 537
                    self.match(python_grammarParser.POINTS)


                self.state = 541
                localctx.end = self.expr(0)
                self.state = 542
                self.match(python_grammarParser.CBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(python_grammarParser.ID, 0)

        def POINTS(self):
            return self.getToken(python_grammarParser.POINTS, 0)

        def expr(self):
            return self.getTypedRuleContext(python_grammarParser.ExprContext,0)


        def STRING(self):
            return self.getToken(python_grammarParser.STRING, 0)

        def INT(self):
            return self.getToken(python_grammarParser.INT, 0)

        def getRuleIndex(self):
            return python_grammarParser.RULE_keyvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyvalue" ):
                listener.enterKeyvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyvalue" ):
                listener.exitKeyvalue(self)




    def keyvalue(self):

        localctx = python_grammarParser.KeyvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_keyvalue)
        try:
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.match(python_grammarParser.ID)
                self.state = 547
                self.match(python_grammarParser.POINTS)
                self.state = 548
                self.expr(0)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(python_grammarParser.STRING)
                self.state = 550
                self.match(python_grammarParser.POINTS)
                self.state = 551
                self.expr(0)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 552
                self.match(python_grammarParser.INT)
                self.state = 553
                self.match(python_grammarParser.POINTS)
                self.state = 554
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[23] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




