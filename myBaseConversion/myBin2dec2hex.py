'''
Author       : Xu Xiaokang
Email        :
Date         : 2021-11-20 22:19:15
LastEditors  : Xu Xiaokang
LastEditTime : 2024-10-24 11:43:50
Filename     :
Description  :
'''


# %%
def bin2dec(bin_str: str) -> int:
    '''
    函数功能：不带符号位的2进制字符串 -> 10进制整数\n
    输入：2进制字符串，可带正负号，0b，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输出：10进制整数，只保留负号，正号不保留
    '''
    return int(bin_str.strip(), base = 2)


# %%
def bin2hex(bin_str: str, hex_width :int = -1) -> str:
    '''
    函数功能：不带符号位的2进制字符串 -> 不带符号位的16进制字符串\n
    输入参数1：2进制字符串，可带正负号，0b，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，16进制字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干0\n
    输出：16进制字符串，只保留负号，正号不保留
    '''
    new_bin_str = bin_str.strip()
    if (new_bin_str[0] == '+' or new_bin_str[0] == '-'): # 去除正负符号
        new_bin_str = new_bin_str[1:]
    if (new_bin_str[:2] == '0b'):
        new_bin_str = new_bin_str[2:]
    hex_str = hex(int(new_bin_str, base = 2))[2:]
    if (hex_width == -1):
        pass
    elif (hex_width < len(hex_str)): # 位宽小于实际16进制数位宽时
        print('位宽参数' + str(hex_width) + ' < 2进制' + bin_str + '输出16进制' + '0x' + hex_str
            + '实际位宽' + str(len(hex_str)) + '，请修正位宽参数')
    else:
        hex_str = '0' * (hex_width - len(hex_str)) + hex_str # 扩展位补0
    if (bin_str[0] == '-'):
        return '-' + '0x' + hex_str
    else:
        return '0x' + hex_str


# %%
def dec2bin(dec_num: int, bin_width :int = -1) -> str:
    '''
    函数功能：10进制整数/字符串 -> 不带符号位的2进制字符串\n
    输入参数1：10进制整数/字符串，可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，2进制字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干0\n
    输出：16进制字符串，只保留负号，正号不保留
    '''
    input_dec_num = dec_num
    if (type(dec_num) == str):
        dec_num = int(dec_num.strip())
    old_bin_str = bin(dec_num)
    if (old_bin_str[0] == '-'):
        bin_str = old_bin_str[3:]
    else:
        bin_str = old_bin_str[2:]
    if (bin_width == -1):
        pass
    elif (bin_width < len(bin_str)):
        print('位宽参数' + str(bin_width) + ' < 10进制' + str(input_dec_num) + '输出2进制' + old_bin_str
            + '最小需要位宽' + str(len(bin_str)) + '，请修正位宽参数')
    else:
        bin_str = '0' * (bin_width - len(bin_str)) + bin_str
    if (old_bin_str[0] == '-'):
        return '-0b' + bin_str
    else:
        return '0b' + bin_str


# %%
def dec2hex(dec_num: int , hex_width: int = -1) -> str:
    '''
    函数功能：10进制整数/字符串 -> 不带符号位的16进制字符串\n
    输入参数1：10进制整数/字符串，可带正负号，前后可加任意个 \n 和 空格，数字间可加下划线\n
    输入参数2：可选，16进制字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干0\n
    输出：16进制字符串，只保留负号，正号不保留
    '''
    old_hex_str = bin2hex(dec2bin(dec_num))
    if (old_hex_str[0] == '-'):
        hex_str = old_hex_str[3:]
    else:
        hex_str = old_hex_str[2:]
    if (hex_width == -1):
        pass
    elif (hex_width < len(hex_str)):
        print('位宽参数' + str(hex_width) + ' < 10进制' + str(dec_num) + '输出16进制' + old_hex_str
            + '实际位宽' + str(len(hex_str)) + '，请修正位宽参数')
    else:
        hex_str = '0' * (hex_width - len(hex_str)) + hex_str
    if (old_hex_str[0] == '-'):
        return '-0x' + hex_str
    else:
        return '0x' + hex_str


# %%
def hex2dec(hex_str: str) -> int:
    '''
    函数功能：不带符号位的16进制字符串 -> 10进制整数\n
    输入：16进制字符串，可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输出：10进制整数，只保留负号，正号不保留
    '''
    return int(hex_str.strip(), base = 16)


# %%
def hex2bin(hex_str: str, bin_width = -1) -> str:
    '''
    函数功能：不带符号位的16进制字符串 -> 不带符号位的2进制字符串\n
    输入：16进制字符串，可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，2进制字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干0\n
    输出：2进制字符串，只保留负号，正号不保留
    '''
    old_bin_str = dec2bin(hex2dec(hex_str))
    if (old_bin_str[0] == '-'):
        bin_str = old_bin_str[3:]
    else:
        bin_str = old_bin_str[2:]
    if (bin_width == -1):
        pass
    elif (bin_width < len(bin_str)):
        print('位宽参数' + str(bin_width) + ' < 16进制' + hex_str + '输出2进制' + old_bin_str
            + '实际位宽' + str(len(bin_str)) + '，请修正位宽参数')
    else:
        bin_str = '0' * (bin_width - len(bin_str)) + bin_str
    if (old_bin_str[0] == '-'):
        return '-0b' + bin_str
    else:
        return '0b' + bin_str


# %%
def signed_bin2dec(bin_str: str) -> int:
    '''
    函数功能：2进制补码字符串 -> 10进制整数\n
    输入：2进制补码字符串，不可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输出：10进制整数，只保留负号，正号不保留
    '''
    bin_str = bin_str.strip()
    if (bin_str[:2] == '0b'):
        if (bin_str[2] == '_'):
            bin_str = bin_str[3:]
        else:
            bin_str = bin_str[2:]
    if (bin_str[0] == '_'):
        int ('输入 ' + bin_str + ' 不合法，首字符不能是下划线 且 不允许出现连续两个下划线')
    elif (bin_str[0] == '0'):
        return int(bin_str, base = 2)
    elif (bin_str[0] == '1'):
        a = int(bin_str, base = 2) # 此语句可检查输入是否合法
        bin_str = bin_str.replace('_', '')
        return a - 2**len(bin_str)
    else:
        int('输入 ' + bin_str + ' 不合法，必须为2进制补码，不允许带正负号')


# %%
def fourBin2OneHex(four_bin: str) -> str:
    '''
    函数功能：4位2进制字符串 -> 1位16进制字符串\n
    输入：4位2进制字符串，输入范围0000~1111\n
    输出：1位16进制字符串
    '''
    if (four_bin == '0000'):
        return '0'
    elif (four_bin == '0001'):
        return '1'
    elif (four_bin == '0010'):
        return '2'
    elif (four_bin == '0011'):
        return '3'
    elif (four_bin == '0100'):
        return '4'
    elif (four_bin == '0101'):
        return '5'
    elif (four_bin == '0110'):
        return '6'
    elif (four_bin == '0111'):
        return '7'
    elif (four_bin == '1000'):
        return '8'
    elif (four_bin == '1001'):
        return '9'
    elif (four_bin == '1010'):
        return 'a'
    elif (four_bin == '1011'):
        return 'b'
    elif (four_bin == '1100'):
        return 'c'
    elif (four_bin == '1101'):
        return 'd'
    elif (four_bin == '1110'):
        return 'e'
    elif (four_bin == '1111'):
        return 'f'
    else:
        int('输入2进制字符' + four_bin + '错误，2进制只能包含0或1')

def signed_bin2hex(bin_str: str, hex_width: int = -1) -> str:
    '''
    函数功能：2进制补码字符串 -> 16进制补码字符串\n
    输入参数1：2进制补码字符串，不可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，16进制补码字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干符号位\n
    输出：16进制补码字符串
    '''
    input_bin_str = bin_str
    bin_str = bin_str.strip()
    if (bin_str[:2] == '0b'): # 2进制字符串以0b开头
        bin_str = bin_str[2:]
    elif (bin_str[0] == '0' or bin_str[0] == '1'):
        pass
    else:
        int('输入 ' + bin_str + ' 不合法，输入必须为2进制补码，不允许带正负号 且 首字符不能是下划线')
    # 检查输入是否合法，末尾字符不能是下划线 且 不能出现连续的两个下划线
    if (bin_str[-1] == '_' or '__' in bin_str):
        int('输入 ' + bin_str + ' 不合法，末尾字符不能是下划线 且 不能出现连续的两个下划线')
    else:
        bin_str = bin_str.replace('_', '') # 输入合法则去除下划线
    # 去掉2进制补码字符串前面多余的符号位，保留两位
    for i in range(len(bin_str)-1):
        if (bin_str[i+1] == bin_str[0]):
            if (i + 1 == len(bin_str)-1):
                bin_str = bin_str[i:]
            else:
                continue
        else:
            bin_str = bin_str[i:]
            break
    if (len(bin_str) % 4 > 0): # 补符号位到位宽为4的倍数
        bin_str = bin_str[0] * (4 - len(bin_str) % 4) + bin_str
    hex_str = ''
    for i in range(int(len(bin_str)/4)):
        hex_str += fourBin2OneHex(bin_str[i*4 : i*4+4])
    if (hex_width == -1):
        pass
    elif (hex_width < len(hex_str)):
        print('位宽参数' + str(hex_width) + ' < 2进制补码' + input_bin_str + '输出16进制补码'
            + '0x' + hex_str +'实际位宽' + str(len(hex_str)) + '，请修正位宽参数')
    else:
        if (hex_str[0] in ['0', '1', '2', '3', '4', '5', '6', '7']):
            hex_str = '0' * (hex_width - len(hex_str)) + hex_str
        else:
            hex_str = 'f' * (hex_width - len(hex_str)) + hex_str
    return '0x' + hex_str


# %%
def signed_dec2bin(dec_num: int, bin_width: int = -1) -> str:
    '''
    函数功能：10进制数/字符串 -> 2进制补码字符串\n
    输入参数1：10进制数/字符串，可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，2进制补码字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干符号位\n
    输出：2进制补码字符串
    '''
    dec_num_str = str(dec_num)
    if (type(dec_num) == str):
        dec_num = int(dec_num.strip())
    if (dec_num == 0):
        bin_str = '0'
    elif (dec_num > 0):
        bin_str = '0' + bin(dec_num)[2:] # 补符号位0
    else:
        for i in range(10000):
            if (2**i + dec_num >= 0):
                bin_str = bin(2**(i+1) + dec_num)[2:] # 一个负数num的补码等于（2**i + dec_num)
                break
    if (bin_width == -1):
        pass
    elif (bin_width < len(bin_str)):
        # 实际位宽大于设定位宽则报警告，然后按实际位宽输出
        print('位宽参数' + str(bin_width) + ' < 10进制' + dec_num_str + '输出2进制补码'
            + '0b' + bin_str + '实际位宽' + str(len(bin_str)) + '，请修正位宽参数')
    else:
        bin_str = bin_str[0] * (bin_width - len(bin_str)) + bin_str # 实际位宽小于设定位宽则补符号位
    return '0b' + bin_str


# %%
def signed_dec2hex(dec_num: int, hex_width = -1) -> str:
    '''
    函数功能：10进制数/字符串 -> 16进制补码字符串\n
    输入参数1：10进制数/字符串，可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线_\n
    输入参数2：可选，16进制补码字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干符号位\n
    输出：16进制补码字符串
    '''
    hex_str = signed_bin2hex(signed_dec2bin(dec_num))[2:]
    if (hex_width == -1):
        pass
    elif (hex_width < len(hex_str)):
        print('位宽参数' + str(hex_width) + ' < 10进制' + str(dec_num) + '输出16进制补码' + '0x' +
            hex_str + '实际位宽' + str(len(hex_str)) + '，请修正位宽参数')
    else:
        if (hex_str[0] in ['0', '1', '2', '3', '4', '5', '6', '7']):
            hex_str = '0' * (hex_width - len(hex_str)) + hex_str
        else:
            hex_str = 'f' * (hex_width - len(hex_str)) + hex_str
    return '0x' + hex_str


# %%
def oneHex2fourBin(one_hex: str) -> str:
    '''
    函数功能：1位16进制字符串 -> 4位2进制字符串\n
    输入：1位16进制字符串，输入范围0~9, a~f或A~F\n
    输出：4位2进制字符串
    '''
    if (one_hex == '0'):
        return '0000'
    elif (one_hex == '1'):
        return '0001'
    elif (one_hex == '2'):
        return '0010'
    elif (one_hex == '3'):
        return '0011'
    elif (one_hex == '4'):
        return '0100'
    elif (one_hex == '5'):
        return '0101'
    elif (one_hex == '6'):
        return '0110'
    elif (one_hex == '7'):
        return '0111'
    elif (one_hex == '8'):
        return '1000'
    elif (one_hex == '9'):
        return '1001'
    elif (one_hex == 'a' or one_hex == 'A'):
        return '1010'
    elif (one_hex == 'b' or one_hex == 'B'):
        return '1011'
    elif (one_hex == 'c' or one_hex == 'C'):
        return '1100'
    elif (one_hex == 'd' or one_hex == 'D'):
        return '1101'
    elif (one_hex == 'e' or one_hex == 'E'):
        return '1110'
    elif (one_hex == 'f' or one_hex == 'F'):
        return '1111'
    else:
        int('输入16进制字符' + one_hex + '错误，16进制只能包含0~9, a~f或A~F')

def signed_hex2bin(hex_str: str, bin_width: int = -1) -> str:
    '''
    函数功能：16进制补码字符串 -> 2进制补码字符串\n
    输入参数1：16进制补码字符串，不可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输入参数2：可选，2进制补码字符串宽度，若实际输出宽度>此参数，警告并原样输出；若实际输出宽度<=此参数，高位补若干符号位\n
    输出：2进制补码字符串
    '''
    input_hex_str = hex_str
    hex_str = hex_str.strip()
    # 检查输入是否合法，不允许带正负号，首尾不能是下划线，不能出现连续两个下划线
    if (hex_str[0] in ['+', '-', '_'] or hex_str[-1] == '_' or '__' in hex_str):
        int('输入' + input_hex_str + '不合法，必须为16进制补码，不允许带正负号, '
            + '首尾不能是下划线，不能出现连续两个下划线')
    elif (hex_str[:2] == '0x'):
        hex_str = hex_str[2:]
    hex_str = hex_str.replace('_', '') # 输入合法则去除下划线
    bin_str = ''
    for i in hex_str:
        bin_str += oneHex2fourBin(i)
    # 去掉2进制补码字符串前面多余的符号位，保留两位
    for i in range(len(bin_str)-1):
        if (bin_str[i+1] == bin_str[0]):
            if (i + 1 == len(bin_str)-1):
                bin_str = bin_str[i:]
            else:
                continue
        else:
            bin_str = bin_str[i:]
            break
    if (bin_str == '00'):
        bin_str = '0'
    if (bin_width == -1):
        pass
    elif (bin_width < len(bin_str)):
        # 实际位宽大于设定位宽则报警告，然后按实际位宽输出
        print('位宽参数' + str(bin_width) + ' < 16进制补码' + input_hex_str + '输出2进制补码'
            + '0b' + bin_str + '实际位宽' + str(len(bin_str)) + '，请修正位宽参数')
    else:
        bin_str = bin_str[0] * (bin_width - len(bin_str)) + bin_str # 实际位宽小于设定位宽则补符号位
    return '0b' + bin_str


# %%
def signed_hex2dec(hex_str: str) -> int:
    '''
    函数功能：16进制补码字符串 -> 10进制整数\n
    输入：16进制补码字符串，不可带正负号，前后可加任意个 \\n 和 空格，数字间可加下划线\n
    输出：10进制整数，只保留负号，正号不保留
    '''
    return signed_bin2dec(signed_hex2bin(hex_str))

# %%
def XQN_dec2bin(dec, X: int, N: int):
    '''
    函数功能: 带符号位的10进制数/字符串 -> XQN格式的二进制字符串\n
    输入1: dec, 10进制数/字符串, 可带正负号, 前后可加任意个 \\n 和 空格, 数字间可加下划线\n
    输入2: X, 非负整数, 表示整数位宽, 默认值0, 表示默认可转换的数的范围是(-1, +1)\n
    输入3: N, 非负整数, 表示小数位宽, 默认值15, 表示默认以15位二进制表示小数部分\n
    输出: 以XQN格式表示的二进制补码字符串, 组成为: 前缀0b + 符号1位 + 整数X位 + 小数N位\n
    使用注意: 1.输入dec的范围必须是[-2**X, 2**X), 超出此范围程序会报错\n
            2.N=0表示小数位为0, 则结果为整数位的补码\n
    编程思路: 输入参数有效性检测 -> 整数部分小数部分分离 -> 分别求二进制原码 -> \n
            对于负数, 将符号位, 整数, 小数三部分组合起来, 求二进制补码, 补码的计算方法为\n
            符号位不变, 其余位取反, 最后连上符号位, 再+1, 取低有效位作为结果
    '''
    def XQN_singelDec2bin(dec, X, N):
        # 记录原始输入值
        input_dec = str(dec)
        # 去除无关字符, 并检查输入dec是否有效
        dec = float(str(dec).strip())

        # 检查输入X和N是否有效
        if (not isinstance(X, int) or X < 0):
            int('整数位宽X必须为非负整数')
        if (not isinstance(N, int) or N < 0):
            int('小数位宽N必须为非负整数')
        if (dec < -(2**X) or dec >= 2**X):
            # 无法表示此范围以外的数, 如X=0, 则最大表示范围为[-1.0, 1), 无法表示-1.5, 因为会和-0.5同值
            # 同理如X=1, 无法表示-2.5, 因为会和-0.5同值
            int(f'{1+X}位二进制补码最大表示范围为[{-2**X} : {2**X}), 输入{input_dec}无法表示')

        dec_is_positive_number = True # 正数标志位
        # 如果dec为+0或者-0, 则直接返回全0
        if (dec == 0):
            return '0b' + '0' * (1 + X + N)
        elif (dec < 0):
            dec_is_positive_number = False

        # 分割整数部分和小数部分
        integer_part = int(dec)
        decimal_part = abs(dec - integer_part)

        # 转换整数部分
        integer_binary = bin(abs(integer_part))[2:].zfill(X)

        # 转换小数部分
        decimal_binary = ''
        for _ in range(N):
            decimal_part *= 2
            bit = int(decimal_part)
            decimal_binary += str(bit)
            decimal_part -= bit

        # 拼接结果
        if dec_is_positive_number:
            result = ('0' + integer_binary + decimal_binary)[-(X+N+1):]
        else:
            binary_value = integer_binary + decimal_binary
            # 除符号位外按位取反
            inverted_bits  = '1' + ''.join('1' if bit == '0' else '0' for bit in binary_value)
            # 加 1, 并取低位, 若1111 + 1后位宽增加, 则只取低位的0
            result = bin(int(inverted_bits , 2) + 1)[2:][-(X+N+1):]

        return '0b' + result

    # 如果输入dec是列表或是元组, 则便利其中的数据, 调用单个元素处理函数, 再拼接为列表输出
    if (isinstance(dec, list) or isinstance(dec, tuple)):
        bin_ls = []
        for i in dec:
            bin_ls.append(XQN_singelDec2bin(i, X, N))
        return bin_ls
    else:
        return XQN_singelDec2bin(dec, X, N)

# %%
def XQN_bin2dec(bin_str: str, X: int):
    '''
    函数功能:  XQN格式的二进制字符串 -> 带符号位的10进制小数, XQN组成为: (前缀0b) + 符号1位 + 整数X位 + 小数N位\n
    输入1: bin_str, 2进制补码字符串, 不能带正负号, 能以0b开头, 前后可加任意个 \\n 和 空格, 数字间可加下划线\n
    输入2: X, 非负整数, 表示整数位宽, 默认值0, 表示默认可转换的数的范围是[-1, +1)\n
    输出: 带符号位的10进制小数\n
    编程思路: 输入参数有效性检测 -> 判断正负 -> 正数则直接调用int(bin_str, base=2)转10进制\n
            -> 对于负数, 其10进制 = int(bin_str, base=2) - 2**len(bin_str)\n
            -> 对于X位整数的XQN格式, 其10进制数为原始10进制数的1/(2**(len(bin_str)-X-1))倍
    '''
    dec = 0
    bin_str = bin_str.strip()
    if (bin_str[:2] == '0b'):
        bin_str = bin_str[2:]
    if (bin_str[0] == '0'):
        dec = int(bin_str, base = 2)
    elif (bin_str[0] == '1'):
        a = int(bin_str, base = 2) # 此语句可检查输入是否合法
        bin_str = bin_str.replace('_', '')
        dec = a - 2**len(bin_str)
    else:
        int('输入 ' + bin_str + ' 不合法, 必须为2进制补码, 不允许带正负号')
    dec = dec / (2**(len(bin_str)-X-1))
    return dec