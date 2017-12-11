str = 'X-DSPAM-Confidence:0.8475'
where = (str.find(":") + 1)
newStr = str[where:]
value = float(newStr)
