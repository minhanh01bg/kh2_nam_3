# abc = [22, 44, 66, 88, 2002, 2222, 2442, 2662, 2882, 4004, 4224, 4444, 4664, 4884, 6006, 6226, 6446, 6666, 6886,
#  8008, 8228, 8448, 8668, 8888, 200002, 202202, 204402, 206602, 208802, 220022, 222222, 224422, 226622, 228822, 
#  240042, 242242, 244442, 246642, 248842, 260062, 262262, 264462, 266662, 268862, 280082, 282282, 284482, 286682, 
#  288882, 400004, 402204, 404404, 406604, 408804, 420024, 422224, 424424, 426624, 428824, 440044, 442244, 444444,
#   446644, 448844, 460064, 462264, 464464, 466664, 468864, 480084, 482284, 484484, 486684, 488884, 600006, 602206,
#    604406, 606606, 608806, 620026, 622226, 624426, 626626, 628826, 640046, 642246, 644446, 646646, 648846, 660066,
#     662266, 664466, 666666, 668866, 680086, 682286, 684486, 686686, 688886, 800008, 802208, 804408, 806608, 808808,
#      820028, 822228, 824428, 826628, 828828, 840048, 842248, 844448, 846648, 848848, 860068, 862268, 864468, 866668,
#  868868, 880088, 882288, 884488, 886688, 888888, 20000002, 20022002, 20044002, 20066002, 20088002, 20200202, 20222202,
#   20244202, 20266202, 20288202, 20400402, 20422402, 20444402, 20466402, 20488402, 20600602, 20622602, 20644602, 20666602,
#    20688602, 20800802, 20822802, 20844802, 20866802, 20888802, 22000022, 22022022, 22044022, 22066022, 22088022, 22200222, 
#    22222222, 22244222, 22266222, 22288222, 22400422, 22422422, 22444422, 22466422, 22488422, 22600622, 22622622, 22644622, 
#    22666622, 22688622, 22800822, 22822822, 22844822, 22866822, 22888822, 24000042, 24022042, 24044042, 24066042, 24088042, 
# 24200242, 24222242, 24244242, 24266242, 24288242, 24400442, 24422442, 24444442, 24466442, 24488442, 24600642, 24622642, 
# 24644642, 24666642, 24688642, 24800842, 24822842, 24844842, 24866842, 24888842, 26000062, 26022062, 26044062, 26066062, 
# 26088062, 26200262, 26222262, 26244262, 26266262, 26288262, 26400462, 26422462, 26444462, 26466462, 26488462, 26600662, 
# 26622662, 26644662, 26666662, 26688662, 26800862, 26822862, 26844862, 26866862, 26888862, 28000082, 28022082, 28044082, 
# 28066082, 28088082, 28200282, 28222282, 28244282, 28266282, 28288282, 28400482, 28422482, 28444482, 28466482, 28488482,
#  28600682, 28622682, 28644682, 28666682, 28688682, 28800882, 28822882, 28844882, 28866882, 28888882, 40000004, 40022004,
#   40044004, 40066004, 40088004, 40200204, 40222204, 40244204, 40266204, 40288204, 40400404, 40422404, 40444404, 40466404,
#    40488404, 40600604, 40622604, 40644604, 40666604, 40688604, 40800804, 40822804, 40844804, 40866804, 40888804, 42000024,
#     42022024, 42044024, 42066024, 42088024, 42200224, 42222224, 
# 42244224, 42266224, 42288224, 42400424, 42422424, 42444424, 42466424, 42488424, 42600624, 42622624, 42644624, 
# 42666624, 42688624, 42800824, 42822824, 42844824, 42866824, 42888824, 44000044, 44022044, 44044044, 44066044,
#  44088044, 44200244, 44222244, 44244244, 44266244, 44288244, 44400444, 44422444, 44444444, 44466444, 44488444, 
#  44600644, 44622644, 44644644, 44666644, 44688644, 44800844, 44822844, 44844844, 44866844, 44888844, 46000064, 
#  46022064, 46044064, 46066064, 46088064, 46200264, 46222264, 46244264, 46266264, 46288264, 46400464, 46422464, 
#  46444464, 46466464, 46488464, 46600664, 46622664, 46644664, 46666664, 46688664, 46800864, 46822864, 46844864,
#   46866864, 46888864, 48000084, 48022084, 48044084, 48066084, 48088084, 48200284, 48222284, 48244284, 48266284,
#    48288284, 48400484, 48422484, 48444484, 48466484, 48488484, 48600684, 48622684, 48644684, 48666684, 48688684,
#     48800884, 48822884, 48844884, 48866884, 48888884, 60000006, 60022006, 60044006, 60066006, 60088006, 60200206, 
#     60222206, 60244206, 60266206, 60288206, 60400406, 60422406, 60444406, 60466406, 60488406, 60600606, 60622606, 
#     60644606, 60666606, 60688606, 60800806, 60822806, 60844806, 60866806, 60888806, 62000026, 62022026, 62044026, 
#     62066026, 62088026, 62200226, 62222226, 62244226, 62266226, 62288226, 62400426, 62422426, 62444426, 62466426, 
#     62488426, 62600626, 62622626, 62644626, 62666626, 62688626, 62800826, 62822826, 62844826, 62866826, 62888826, 
#     64000046, 64022046, 64044046, 64066046, 64088046, 64200246, 64222246, 64244246, 64266246, 64288246, 64400446, 
#     64422446, 64444446, 64466446, 64488446, 64600646, 64622646, 64644646, 64666646, 64688646, 64800846, 64822846, 
#     64844846, 64866846, 64888846, 66000066, 66022066, 66044066, 66066066, 66088066, 66200266, 66222266, 66244266, 
#     66266266, 66288266, 66400466, 
# 66422466, 66444466, 66466466, 66488466, 66600666, 66622666, 66644666, 66666666, 66688666, 66800866, 66822866, 
# 66844866, 66866866, 66888866, 68000086, 68022086, 68044086, 68066086, 68088086, 68200286, 68222286, 68244286, 
# 68266286, 68288286, 68400486, 68422486, 68444486, 68466486, 68488486, 68600686, 68622686, 68644686, 68666686,
#  68688686, 68800886, 68822886, 68844886, 68866886, 68888886, 80000008, 80022008, 80044008, 80066008, 80088008, 
#  80200208, 80222208, 80244208, 80266208, 80288208, 80400408, 80422408, 80444408, 80466408, 80488408, 80600608,
#   80622608, 80644608, 80666608, 80688608, 80800808, 80822808, 80844808, 80866808, 80888808, 82000028, 82022028, 
#   82044028, 82066028, 82088028, 82200228, 82222228, 82244228, 82266228, 82288228, 82400428, 82422428, 82444428, 
#   82466428, 82488428, 82600628, 82622628, 82644628, 82666628, 82688628, 82800828, 82822828, 82844828, 82866828, 
#   82888828, 84000048, 84022048, 84044048, 84066048, 84088048, 84200248, 84222248, 84244248, 84266248, 84288248, 
#   84400448, 84422448, 84444448, 84466448, 84488448, 84600648, 84622648, 84644648, 84666648, 84688648, 84800848, 
#   84822848, 84844848, 84866848, 84888848, 86000068, 86022068, 86044068, 86066068, 86088068, 86200268, 86222268, 
#   86244268, 86266268, 86288268, 86400468, 86422468, 86444468, 86466468, 86488468, 86600668, 86622668, 86644668, 
#   86666668, 86688668, 86800868, 86822868, 86844868, 86866868, 86888868, 88000088, 88022088, 88044088, 88066088, 
#   88088088, 88200288, 88222288, 88244288, 88266288, 88288288, 88400488, 88422488, 88444488, 88466488, 88488488, 88600688, 
# 88622688, 88644688, 88666688, 88688688, 88800888, 88822888, 88844888, 88866888, 88888888]

def check(n):
    m = "".join(reversed(str(n)))
    if(len(m)%2!=0):
        return False
    for i in range(0,len(m)):
        if m[i]!=str(0) and m[i]!=str(2) and m[i]!=str(4) and m[i]!=str(6) and m[i] != str(8):
            return False
    if m == str(n):
        return True
    return False

def solve():
    n = int(input())
    for i in range(22, n, 22):
        if check(i) and i % 2 == 0:
            print(i,end=" ")

if __name__ == "__main__":
    t = int(input())
    while t!=0:
        solve()
        print("")
        t-=1