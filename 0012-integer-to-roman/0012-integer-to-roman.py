class Solution:
    def intToRoman(self, num: int) -> str:
        out = ""
        if num>=1000:
            out = out + "M"*(int(num/1000))
            num = num - (int(num/1000))*1000
        if num>=900:
            out = out + "CM" 
            num = num -900
        if num>=500:
            out = out+"D"
            num = num - 500
        if num>=400:
            out = out+"CD"
            num = num - 400
        if num>=100:
            out = out + "C"*(int(num/100))
            num = num - (int(num/100))*100
        if num>=90:
            out = out + "XC"
            num = num - 90
        if num>=50:
            out = out+"L"
            num = num - 50
        if num>=40:
            out = out + "XL"
            num = num - 40
        if num>=10:
            out = out + "X"*(int(num/10))
            num = num - (int(num/10))*10
        if num>=9:
            out = out + "IX"
            num = num - 9 
        if num >=5:
            out = out + "V"
            num = num -5
        if num == 4:
            out = out + "IV"
            num = num -4
        if num >=1:
            out = out + "I"*num
        return out
