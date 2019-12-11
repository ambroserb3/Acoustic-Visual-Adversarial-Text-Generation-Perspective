import random
from string import ascii_letters
import homoglyphs as hg

#### Phoneme Dictionary ############
Homoglyphs =	{
'a' : ['@', '4', 'À', 'Á', 'Â' ,'Ã', 'Ä', 'Å', 'à', 'á', 'â', 'ã', 'ä', 'å', 'ɑ', 'Α', 'α', 'а', 'Ꭺ', 'Ａ', 'ａ'],
'A' : ['@', '4', 'À', 'Á', 'Â' ,'Ã', 'Ä', 'Å', 'à', 'á', 'â', 'ã', 'ä', 'å', 'ɑ', 'Α', 'α', 'а', 'Ꭺ', 'Ａ', 'ａ'],
'b':['B','b','ß','ʙ','Β','β','В','Ь','Ᏼ','ᛒ','Ｂ','ｂ'], 
'B':['B','b','ß','ʙ','Β','β','В','Ь','Ᏼ','ᛒ','Ｂ','ｂ'], 
'c':['C','c','ϲ','Ϲ','С','с','Ꮯ','Ⅽ','ⅽ','𐐠','Ｃ','ｃ'],
'C':['C','c','ϲ','Ϲ','С','с','Ꮯ','Ⅽ','ⅽ','𐐠','Ｃ','ｃ'],
'd':['D','d','Ď','ď','Đ','đ','ԁ','ժ','Ꭰ','ḍ','Ⅾ','ⅾ','Ｄ','ｄ'],
'D':['D','d','Ď','ď','Đ','đ','ԁ','ժ','Ꭰ','ḍ','Ⅾ','ⅾ','Ｄ','ｄ'],
'e':['E','e','È','É','Ê','Ë','é','ê','ë','Ē','ē','Ĕ','ĕ','Ė','ė','Ę','Ě','ě','Ε','Е','е','Ꭼ','Ｅ','ｅ'],
'E':['E','e','È','É','Ê','Ë','é','ê','ë','Ē','ē','Ĕ','ĕ','Ė','ė','Ę','Ě','ě','Ε','Е','е','Ꭼ','Ｅ','ｅ'],
'f':['F','f','Ϝ','Ｆ','ｆ'],
'F':['F','f','Ϝ','Ｆ','ｆ'],
'g':['G','g','ɡ','ɢ','Ԍ','ն','Ꮐ','Ｇ','ｇ'],
'G':['G','g','ɡ','ɢ','Ԍ','ն','Ꮐ','Ｇ','ｇ'],
'h':['H' 'h' 'ʜ' 'Η' 'Н' 'һ' 'Ꮋ' 'Ｈ' 'ｈ'],
'H':['H' 'h' 'ʜ' 'Η' 'Н' 'һ' 'Ꮋ' 'Ｈ' 'ｈ'],
'i':['I','i','l','ɩ','Ι','І','і','ا','Ꭵ','ᛁ','Ⅰ','ⅰ','ｉ'],
'I':['I','i','l','ɩ','Ι','І','і','ا','Ꭵ','ᛁ','Ⅰ','ⅰ','ｉ'],
'j':['J','j','ϳ','Ј','ј','յ','Ꭻ','Ｊ','ｊ'],
'J':['J','j','ϳ','Ј','ј','յ','Ꭻ','Ｊ','ｊ'],
'k':['K','k','Κ','κ','К','Ꮶ','ᛕ','K','Ｋ','ｋ'],
'K':['K','k','Κ','κ','К','Ꮶ','ᛕ','K','Ｋ','ｋ'],
'l':['L','l','ʟ','ι','ا','Ꮮ','Ⅼ','ⅼ','Ｌ','ｌ'],
'L':['L','l','ʟ','ι','ا','Ꮮ','Ⅼ','ⅼ','Ｌ','ｌ'],
'm':['M','m','Μ','Ϻ','М','Ꮇ','ᛖ','Ⅿ','ⅿ','Ｍ','ｍ'],
'M':['M','m','Μ','Ϻ','М','Ꮇ','ᛖ','Ⅿ','ⅿ','Ｍ','ｍ'],
'n':['N','n','ɴ','Ν','Ｎ','ｎ'],
'N':['N','n','ɴ','Ν','Ｎ','ｎ'],
'o':['Ө','σ','ð','Ø','o','օ','O','ᓍ','o̴','o̷','o̳','o̾','o͎','o͓̽','Ỗ','ⓞ','σ','𝓸','𝓞','𝕆','𝐎'], 
'O':['Ө','σ','ð','Ø','o','օ','O','ᓍ','o̴','o̷','o̳','o̾','o͎','o͓̽','Ỗ','ⓞ','σ','𝓸','𝓞','𝕆','𝐎'], 
'p':['p','P','𝔭','𝓹','𝓅','𝕡','ｐ','🄿','Ꭾ','℘','p','𝐩','𝘱','𝙥','𝚙','P','ρ','þ','₱','卩','ｱ','ք','ᑭ','ᕵ','p̴','p̷', 'p̲','p̳','p̾','Ⓟ','Ƥ','𝐏','𝓹'],  
'P':['p','P','𝔭','𝓹','𝓅','𝕡','ｐ','🄿','Ꭾ','℘','p','𝐩','𝘱','𝙥','𝚙','P','ρ','þ','₱','卩','ｱ','ք','ᑭ','ᕵ','p̴','p̷' ,'p̲','p̳','p̾','Ⓟ','Ƥ','𝐏','𝓹'],  
'q':['q','Q','𝔮','𝓆','𝕢','ｑ','Q','🅀','ⓠ','ợ','ϙ','զ','Ꭴ','𝚚','Ɋ','q̴' ,'q̳','q̾','ℚ','Ω','Ｑ'],   
'Q':['q','Q','𝔮','𝓆','𝕢','ｑ','Q','🅀','ⓠ','ợ','ϙ','զ','Ꭴ','𝚚','Ɋ','q̴' ,'q̲','q̳','q̾','ℚ','Ω','Ｑ'],  
'r':['r','R','r','ʀ','Ի','Ꮢ','ᚱ','Ｒ','ｒ'],
'R':['r','R','r','ʀ','Ի','Ꮢ','ᚱ','Ｒ','ｒ'],
's':['s','S','𝔰','𝓈','𝕤','🅂','ꙅ','ⓢ','ร','ʂ','ֆ','Ꮥ','Ş','§','₴','s̴','s̷','s̳','s̾'],
'S':['s','S','𝔰','𝓈','𝕤','🅂','ꙅ','ⓢ','ร','ʂ','ֆ','Ꮥ','Ş','§','₴','s̴','s̷','s̳','s̾'],
't':['t','T','𝔱','𝓉','𝕥','ʇ','🅃','ƚ','ⓣ','ȶ','Ƭ','†','₮','ㄒ','ｲ','է','t̴','t̷','t͎','Ŧ','𝓣'], 
'T':['t','T','𝔱','𝓉','𝕥','ʇ','🅃','ƚ','ⓣ','ȶ','Ƭ','†','₮','ㄒ','ｲ','է','t̴','t̷','t͎','Ŧ','𝓣'], 
'u':['u','U','𝔲','𝓊','𝕦','🅄','ⓤ','ย','υ','ʊ','Ꮼ','ų','น','Ц','µ','Ʉ','ㄩ','ひ','մ','ᑘ','u̷' ,'u̾','u͎','ù','𝕌','Ữ'],
'U':['u','U','𝔲','𝓊','𝕦','🅄','ⓤ','ย','υ','ʊ','Ꮼ','ų','น','Ц','µ','Ʉ','ㄩ','ひ','մ','ᑘ','u̷' ,'u̾','u͎','ù','𝕌','Ữ'],
'v':['v','V','𝔳','𝓋','𝕧','ʌ','🅅','ⓥ','ש','ʋ','Ꮙ','ง','√','ᐺ','v̴','v̷','v͎','v͓̽','Ѷ'],
'V':['v','V','𝔳','𝓋','𝕧','ʌ','🅅','ⓥ','ש','ʋ','Ꮙ','ง','√','ᐺ','v̴','v̷','v͎','v͓̽','Ѷ'],
'w':['w','W','𝔴','ฬ','𝓌','𝕨','ʍ','🅆','ⓦ','ɯ','Ꮗ','ῳ','ຟ','Щ','₩','山'],
'W':['w','W','𝔴','ฬ','𝓌','𝕨','ʍ','🅆','ⓦ','ɯ','Ꮗ','ῳ','ຟ','Щ','₩','山'],
'x':['x','X','𝔵','𝓍','𝕩','🅇','א','Ӽ','ጀ','ҳ','Ӿ','乂','ﾒ','x̴','x̾','x͎','Ж','ⓧ'], 
'X':['x','X','𝔵','𝓍','𝕩','🅇','א','Ӽ','ጀ','ҳ','Ӿ','乂','ﾒ','x̴','x̾','x͎','Ж','ⓧ'],
'y':['y','Y','𝔶','Ў','𝓎','𝕪','ʏ','ʎ','🅈','ⓨ','ץ','ყ','ฯ','¥','ㄚ','ﾘ','վ','ᖻ','y̷' ,'y̾'],
'Y':['y','Y','𝔶','Ў','𝓎','𝕪','ʏ','ʎ','🅈','ⓨ','ץ','ყ','ฯ','¥','ㄚ','ﾘ','վ','ᖻ','y̷' ,'y̾'],
'z':['z','Z','𝔷','ℤ','𝓏','𝕫','🅉','ƹ','ⓩ','չ','ȥ','ፚ','ʑ','ຊ','乙','Հ','z̴','ž'],
'Z':['z','Z','𝔷','ℤ','𝓏','𝕫','🅉','ƹ','ⓩ','չ','ȥ','ፚ','ʑ','ຊ','乙','Հ','z̴','ž']
}


def VisualAttack(word, edit_distance):
    """
    This function takes in a word and replaces random characters with visually similar homoglyphs

    @param word: word to be attacked
    @param edit distance: amount of characters to change.
    """
    # If you just want to change chars that are not whitespace and not the same char in regards to index,
    #  you can first pull the indexes where the non-whitespace chars are:
    inds = [i for i,_ in enumerate(word)]
    # print(word)
    if (edit_distance<len(word)):
        sam = random.sample(inds, edit_distance)
        #Then use those indexes to replace.
        lst = list(word)
        for ind in sam:
            text = lst[ind] 
            if text in Homoglyphs:
                #### Homemade dictionary implementation
                homoglyph = Homoglyphs[text]   
                #replace letter
                lst[ind] = random.choice(homoglyph)
            else: 
                # get homoglyphs (latin alphabet initialized by default) 
                homo = hg.Homoglyphs().get_combinations(text)   #ex: ['q', '𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔮', '𝕢', '𝖖',
                # print(homo)

                #replace letter
                lst[ind] = random.choice(homo)
    else:
        lst = list(word)
        for ind in lst:
            if ind in Homoglyphs:
                #### Homemade dictionary implementation
                homoglyph = Homoglyphs[ind]   
                #replace letter
                ind = random.choice(homoglyph)
            else: 
                # get homoglyphs (latin alphabet initialized by default) 
                homo = hg.Homoglyphs().get_combinations(ind)   #ex: ['q', '𝐪', '𝑞', '𝒒', '𝓆', '𝓺', '𝔮', '𝕢', '𝖖',
                # print(homo)

                #replace letter
                ind = random.choice(homo)
    return "".join(lst)

def Find_Homoglyphs(word, factor, edit_distance):
    """
    This function takes in a word and replaces random characters with visually similar homoglyphs, 
    and returns a list of those word replacements.

    @param word: word to be attacked
    @param edit distance: amount of characters to change.
    @param factor: Integer. How many different words to substitute per index.
    """
    for x in range(factor):
        words = VisualAttack(word, edit_distance)
        # print(words)

    return words

if __name__ == '__main__':
    # VisualAttack("adriano")
    Find_Homoglyphs("hate", 5, 2)