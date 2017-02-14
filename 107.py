# https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
# https://en.wikipedia.org/wiki/Prim%27s_algorithm
# https://en.wikipedia.org/wiki/Minimum_spanning_tree




if __name__ == "__main__":
    network_file = [
        [None, None, None, 427, 668, 495, 377, 678, None, 177, None, None, 870, None, 869, 624, 300, 609, 131, None, 251, None, None, None, 856, 221, 514, None, 591, 762, 182, 56, None, 884, 412, 273, 636, None, None, 774],
        [None, None, 262, None, None, 508, 472, 799, None, 956, 578, 363, 940, 143, None, 162, 122, 910, None, 729, 802, 941, 922, 573, 531, 539, 667, 607, None, 920, None, None, 315, 649, 937, None, 185, 102, 636, 289],
        [None, 262, None, None, 926, None, 958, 158, 647, 47, 621, 264, 81, None, 402, 813, 649, 386, 252, 391, 264, 637, 349, None, None, None, 108, None, 727, 225, 578, 699, None, 898, 294, None, 575, 168, 432, 833],
        [427, None, None, None, 366, None, None, 635, None, 32, 962, 468, 893, 854, 718, 427, 448, 916, 258, None, 760, 909, 529, 311, 404, None, None, 588, 680, 875, None, 615, None, 409, 758, 221, None, None, 76, 257],
        [668, None, 926, 366, None, None, None, 250, 268, None, 503, 944, None, 677, None, 727, 793, 457, 981, 191, None, None, None, 351, 969, 925, 987, 328, 282, 589, None, 873, 477, None, None, 19, 450, None, None, None],
        [495, 508, None, None, None, None, None, 765, 711, 819, 305, 302, 926, None, None, 582, None, 861, None, 683, 293, None, None, 66, None, 27, None, None, 290, None, 786, None, 554, 817, 33, None, 54, 506, 386, 381],
        [377, 472, 958, None, None, None, None, None, None, 120, 42, None, 134, 219, 457, 639, 538, 374, None, None, None, 966, None, None, None, None, None, 449, 120, 797, 358, 232, 550, None, 305, 997, 662, 744, 686, 239],
        [678, 799, 158, 635, 250, 765, None, None, None, 35, None, 106, 385, 652, 160, None, 890, 812, 605, 953, None, None, None, 79, None, 712, 613, 312, 452, None, 978, 900, None, 901, None, None, 225, 533, 770, 722],
        [None, None, 647, None, 268, 711, None, None, None, 283, None, 172, None, 663, 236, 36, 403, 286, 986, None, None, 810, 761, 574, 53, 793, None, None, 777, 330, 936, 883, 286, None, 174, None, None, None, 828, 711],
        [177, 956, 47, 32, None, 819, 120, 35, 283, None, 50, None, 565, 36, 767, 684, 344, 489, 565, None, None, 103, 810, 463, 733, 665, 494, 644, 863, 25, 385, None, 342, 470, None, None, None, 730, 582, 468],
        [None, 578, 621, 962, 503, 305, 42, None, None, 50, None, 155, 519, None, None, 256, 990, 801, 154, 53, 474, 650, 402, None, None, None, 966, None, None, 406, 989, 772, 932, 7, None, 823, 391, None, None, 933],
        [None, 363, 264, 468, 944, 302, None, 106, 172, None, 155, None, None, None, 380, 438, None, 41, 266, None, None, 104, 867, 609, None, 270, 861, None, None, 165, None, 675, 250, 686, 995, 366, 191, None, 433, None],
        [870, 940, 81, 893, None, 926, 134, 385, None, 565, 519, None, None, 313, 851, None, None, None, 248, 220, None, 826, 359, 829, None, 234, 198, 145, 409, 68, 359, None, 814, 218, 186, None, None, 929, 203, None],
        [None, 143, None, 854, 677, None, 219, 652, 663, 36, None, None, 313, None, 132, None, 433, 598, None, None, 168, 870, None, None, None, 128, 437, None, 383, 364, 966, 227, None, None, 807, 993, None, None, 526, 17],
        [869, None, 402, 718, None, None, 457, 160, 236, 767, None, 380, 851, 132, None, None, 596, 903, 613, 730, None, 261, None, 142, 379, 885, 89, None, 848, 258, 112, None, 900, None, None, 818, 639, 268, 600, None],
        [624, 162, 813, 427, 727, 582, 639, None, 36, 684, 256, 438, None, None, None, None, 539, 379, 664, 561, 542, None, 999, 585, None, None, 321, 398, None, None, 950, 68, 193, None, 697, None, 390, 588, 848, None],
        [300, 122, 649, 448, 793, None, 538, 890, 403, 344, 990, None, None, 433, 596, 539, None, None, 73, None, 318, None, None, 500, None, 968, None, 291, None, None, 765, 196, 504, 757, None, 542, None, 395, 227, 148],
        [609, 910, 386, 916, 457, 861, 374, 812, 286, 489, 801, 41, None, 598, 903, 379, None, None, None, 946, 136, 399, None, 941, 707, 156, 757, 258, 251, None, 807, None, None, None, 461, 501, None, None, 616, None],
        [131, None, 252, 258, 981, None, None, 605, 986, 565, 154, 266, 248, None, 613, 664, 73, None, None, 686, None, None, 575, 627, 817, 282, None, 698, 398, 222, None, 649, None, None, None, None, None, 654, None, None],
        [None, 729, 391, None, 191, 683, None, 953, None, None, 53, None, 220, None, 730, 561, None, 946, 686, None, None, 389, 729, 553, 304, 703, 455, 857, 260, None, 991, 182, 351, 477, 867, None, None, 889, 217, 853],
        [251, 802, 264, 760, None, 293, None, None, None, None, 474, None, None, 168, None, 542, 318, 136, None, None, None, None, 392, None, None, None, 267, 407, 27, 651, 80, 927, None, 974, 977, None, None, 457, 117, None],
        [None, 941, 637, 909, None, None, 966, None, 810, 103, 650, 104, 826, 870, 261, None, None, 399, None, 389, None, None, None, 202, None, None, None, None, 867, 140, 403, 962, 785, None, 511, None, 1, None, 707, None],
        [None, 922, 349, 529, None, None, None, None, 761, 810, 402, 867, 359, None, None, 999, None, None, 575, 729, 392, None, None, 388, 939, None, 959, None, 83, 463, 361, None, None, 512, 931, None, 224, 690, 369, None],
        [None, 573, None, 311, 351, 66, None, 79, 574, 463, None, 609, 829, None, 142, 585, 500, 941, 627, 553, None, 202, 388, None, 164, 829, None, 620, 523, 639, 936, None, None, 490, None, 695, None, 505, 109, None],
        [856, 531, None, 404, 969, None, None, None, 53, 733, None, None, None, None, 379, None, None, 707, 817, 304, None, None, 939, 164, None, None, 616, 716, 728, None, 889, 349, None, 963, 150, 447, None, 292, 586, 264],
        [221, 539, None, None, 925, 27, None, 712, 793, 665, None, 270, 234, 128, 885, None, 968, 156, 282, 703, None, None, None, 829, None, None, None, 822, None, None, None, 736, 576, None, 697, 946, 443, None, 205, 194],
        [514, 667, 108, None, 987, None, None, 613, None, 494, 966, 861, 198, 437, 89, 321, None, 757, None, 455, 267, None, 959, None, 616, None, None, None, 349, 156, 339, None, 102, 790, 359, None, 439, 938, 809, 260],
        [None, 607, None, 588, 328, None, 449, 312, None, 644, None, None, 145, None, None, 398, 291, 258, 698, 857, 407, None, None, 620, 716, 822, None, None, 293, 486, 943, None, 779, None, 6, 880, 116, 775, None, 947],
        [591, None, 727, 680, 282, 290, 120, 452, 777, 863, None, None, 409, 383, 848, None, None, 251, 398, 260, 27, 867, 83, 523, 728, None, 349, 293, None, 212, 684, 505, 341, 384, 9, 992, 507, 48, None, None],
        [762, 920, 225, 875, 589, None, 797, None, 330, 25, 406, 165, 68, 364, 258, None, None, None, 222, None, 651, 140, 463, 639, None, None, 156, 486, 212, None, None, 349, 723, None, None, 186, None, 36, 240, 752],
        [182, None, 578, None, None, 786, 358, 978, 936, 385, 989, None, 359, 966, 112, 950, 765, 807, None, 991, 80, 403, 361, 936, 889, None, 339, 943, 684, None, None, 965, 302, 676, 725, None, 327, 134, None, 147],
        [56, None, 699, 615, 873, None, 232, 900, 883, None, 772, 675, None, 227, None, 68, 196, None, 649, 182, 927, 962, None, None, 349, 736, None, None, 505, 349, 965, None, 474, 178, 833, None, None, 555, 853, None],
        [None, 315, None, None, 477, 554, 550, None, 286, 342, 932, 250, 814, None, 900, 193, 504, None, None, 351, None, 785, None, None, None, 576, 102, 779, 341, 723, 302, 474, None, 689, None, None, None, 451, None, None],
        [884, 649, 898, 409, None, 817, None, 901, None, 470, 7, 686, 218, None, None, None, 757, None, None, 477, 974, None, 512, 490, 963, None, 790, None, 384, None, 676, 178, 689, None, 245, 596, 445, None, None, 343],
        [412, 937, 294, 758, None, 33, 305, None, 174, None, None, 995, 186, 807, None, 697, None, 461, None, 867, 977, 511, 931, None, 150, 697, 359, 6, 9, None, 725, 833, None, 245, None, 949, None, 270, None, 112],
        [273, None, None, 221, 19, None, 997, None, None, None, 823, 366, None, 993, 818, None, 542, 501, None, None, None, None, None, 695, 447, 946, None, 880, 992, 186, None, None, None, 596, 949, None, 91, None, 768, 273],
        [636, 185, 575, None, 450, 54, 662, 225, None, None, 391, 191, None, None, 639, 390, None, None, None, None, None, 1, 224, None, None, 443, 439, 116, 507, None, 327, None, None, 445, None, 91, None, 248, None, 344],
        [None, 102, 168, None, None, 506, 744, 533, None, 730, None, None, 929, None, 268, 588, 395, None, 654, 889, 457, None, 690, 505, 292, None, 938, 775, 48, 36, 134, 555, 451, None, 270, None, 248, None, 371, 680],
        [None, 636, 432, 76, None, 386, 686, 770, 828, 582, None, 433, 203, 526, 600, 848, 227, 616, None, 217, 117, 707, 369, 109, 586, 205, 809, None, None, 240, None, 853, None, None, None, 768, None, 371, None, 540],
        [774, 289, 833, 257, None, 381, 239, 722, 711, 468, 933, None, None, 17, None, None, 148, None, None, 853, None, None, None, None, 264, 194, 260, 947, None, 752, 147, None, None, 343, 112, 273, 344, 680, 540, None],
    ]

    dimension = (40, 40)

    original_sum = 0

    '''
        a   b   c   d
    a   x   1   2   3  -> process 1+ (skip 0)
    b   1   x   4   5  -> process 2+ (skip 0-1)
    c   2   4   x   6  -> etc
    d   3   5   6   x  -> etc
    '''


    for i in range(40):
        for j in range(i + 1, 40):
            value = network_file[i][j]        

            if not value:
                continue

            original_sum += value  

    s = 0
    connected = set([0])

    for _ in range(40):
        min_n = float("Inf")
        min_point = None

        for i in range(40):
            if i in connected:
                continue

            for j in connected:
                    if network_file[i][j] and network_file[i][j] < min_n:
                        min_n = network_file[i][j]
                        min_point = i

        if min_point:
            connected.add(min_point)
            s += min_n

    print(original_sum, original_sum-s)
