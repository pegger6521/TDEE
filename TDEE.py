# TDEE = BMR + TEA + TEF 
# 總熱量消耗 = 基礎代謝 + 運動消耗 + 產熱消耗
# TDEE = Total Daily Energy Expenditure

gender = input('請輸入性別: ')
weight = int(input('請輸入體重(公斤): '))
height = int(input('請輸入身高(公分): '))
age = int(input('請輸入年紀: '))
activity_level = input('請輸入活動程度(久坐/每周1-3天/每周3-5天/每周6-7天/每天2次): ')
goal = input('請問您的目標是(維持體重/增加肌肉/減少脂肪): ')

if gender == '女':
    BMR = 10 * weight + 6.25 * height - 5 * age - 161
    if activity_level == '久坐':
        TDEE = 1.2 * BMR
    elif activity_level == '每周1-3天':
        TDEE = 1.375 * BMR
    elif activity_level == '每周3-5天':
        TDEE = 1.55 * BMR
    elif activity_level == '每周6-7天':
        TDEE = 1.725 * BMR
    elif activity_level == '每天2次':
        TDEE = 1.9 * BMR
    print('您的BMR基礎代謝率為:', BMR)
    print('您的TDEE總熱量消耗為:', TDEE)
    if goal == '維持體重':
        print('為了達成', goal,'的目標, 妳要每天吃',TDEE,'卡路里的熱量!')
    elif goal == '增加肌肉':
        print('為了達成', goal,'的目標, 妳要每天吃到',TDEE+300,'卡路里的熱量!')
    elif goal == '減少脂肪':
        print('為了達成', goal,'的目標, 妳每天只能吃',TDEE-300,'卡路里的熱量!')

else:
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
    if activity_level == '久坐':
        TDEE = 1.2 * BMR
    elif activity_level == '每周1-3天':
        TDEE = 1.375 * BMR
    elif activity_level == '每周3-5天':
        TDEE = 1.55 * BMR
    elif activity_level == '每周6-7天':
        TDEE = 1.725 * BMR
    elif activity_level == '每天2次':
        TDEE = 1.9 * BMR
    print('您的BMR基礎代謝率為:', BMR)
    print('您的TDEE總熱量消耗為:', TDEE)
    if goal == '維持體重':
        print('為了達成', goal,'的目標, 你要每天吃',TDEE,'卡路里的熱量!')
    elif goal == '增加肌肉':
        print('為了達成', goal,'的目標, 你要每天吃到',TDEE+300,'卡路里的熱量!')
    elif goal == '減少脂肪':
        print('為了達成', goal,'的目標, 你每天只能吃',TDEE-300,'卡路里的熱量!')


