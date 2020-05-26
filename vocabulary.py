


vocabularies = {"intelligate":"zinnmonn","accountant":"kaikeisi"}


input_word = input("Any help? Expand your vocabulary:")
         # there is a word in vocabulary or not.
new_or = input_word in vocabularies.keys()

if new_or == True: # alredy learned
   print("Again?  the meaning is "+vocabularies[input_word])
elif new_or == False: # new words
    print("new word! wait a sec...")
    from selenium import webdriver

    browser = webdriver.Chrome()

    browser.get('https://www.vocabulary.com/dictionary/')
    elem = browser.find_element_by_xpath('')
    elem.send_keys(input_word)
    btn = browser.find_element_by_xpath('//*[@id="headFixBxTR"]/input')
    btn.click()
    meaning = browser.find_element_by_xpath('//*[@id="summary"]/div[2]/table/tbody/tr/td[2]')
    new_word = meaning.text
    print(new_word)
    browser.quit()
#vocabularies[input_word]=new_word
