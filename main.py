from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
updater = Updater("PYTHON BOT API KEY",use_context=True)
def startFun(update:Update,context:CallbackContext):
    update.message.reply_text("Hello friend welcome to the mockbot.I am designed to help you in your studies,Type /help to see all commands.")
    update.message.reply_text("Select your University-\n"
                              "1-Chaudhary Charan Singh University (/ccsu)\n"
                              "2-Maa Shakumbhari University (/msu\n")
def ccsuMenu(update:Update,context:CallbackContext):
    update.message.reply_text("Select your course below-\n"
                              "/BSE\n"
                              "/BCOM\n"
                              "/BCOM_LLB\n"
                              "/BCA\n"
                              "/LLB\n"
                              "/LLM\n"
                              "/BED\n"
                              "/BBA\n"
                              "/BA_BED\n"
                              "/BFA\n"
                              "/MSC\n"
                              "/MBA\n"
                              "/MED\n"
                              "/BA\n"
                              "/BA_LLB\n"
                              "/BJMC\n"
                              "/BPT\n"
                              "/MA\n"
                              "/MCOM\n"
                              "/MIB\n"
                              "/PHD\n")
def bcom(update:Update,context:CallbackContext):
    update.message.reply_text("Please select your Semester-\n"
                              "/1st_SEM_Bcom\n"
                              "/2nd_SEM_Bcom\n"
                              "/3rd_SEM_Bcom\n"
                              "/4th_SEM_Bcom\n"
                              "/5th_SEM_Bcom\n"
                              "/6th_SEM_Bcom\n")
def firstSemBcom(update:Update,context:CallbackContext):
    update.message.reply_text("Commerce Business Statistics\n"
                              "https://www.ccsustudy.com/papers/bcom-1-sem-commerce-business-statistics-nep-1037-dec-2021.pdf\n"
                              "--------------------------------------------------------------------------------------------------\n"
                              "Commmerce Business Organisation\n"
                              "https://www.ccsustudy.com/papers/bcom-1-sem-major-cource-commerce-business-organisation-nep-1036-dec-2021.pdf\n"
                              "--------------------------------------------------------------------------------------------------\n"
                              "Commerce Business Communication\n"
                              "https://www.ccsustudy.com/papers/bcom-1-sem-major-course-commerce-business-communication-nep-1038-dec-2021.pdf")

def secondSemBcom(update:Update,context:CallbackContext):
    update.message.reply_text("Commerce Business Management\n"
                              "https://www.ccsustudy.com/papers/bcom-2-sem-commerce-business-management-nep-2036-jun-2022.pdf\n")
def bcomLLB(update:Update,context:CallbackContext):
    update.message.reply_text("Please select your Semester-\n"
                              "/1st_SEM_BcomLLB\n"
                              "/2nd_SEM_BcomLLB\n"
                              "/3rd_SEM_BcomLLB\n"
                              "/4th_SEM_BcomLLB\n"
                              "/5th_SEM_BcomLLB\n"
                              "/6th_SEM_BcomLLB\n"
                              "/7th_SEM_BcomLLB\n"
                              "/8th_SEM_BcomLLB\n"
                              "/9th_SEM_BcomLLB\n"
                              "/10th_SEM_BcomLLB\n")
def fifthSemBcomLlb(update:Update,context:CallbackContext):
    update.message.reply_text("Select your subject from below-\n"
                              "/1sub5Bllb Constitutional Law of india \n"
                              "-------------------------------\n"
                              "/2sub5Bllb Contract 2- specific contract and law of partnership\n"
                              "-------------------------------\n"
                              "/3sub5Bllb Jurisprudence legal theory\n"
                              "-------------------------------\n"
                              "/4sub5Bllb Law of crime Indian penal code\n"
                              "-------------------------------\n")
def forthSemBcomLlb(update:Update,context:CallbackContext):
    update.message.reply_text("Select your subject from below-\n"
                              "/1sub4Bllb Auditing \n"
                              "-------------------------------\n"
                              "/2sub4Bllb Financial Management\n"
                              "-------------------------------\n"
                              "/3sub4Bllb Fundamentals of Computer and Information\n"
                              "-------------------------------\n"
                              "/4sub4Bllb Internation Market\n"
                              "-------------------------------\n"
                              "/5sub4Bllb Law of Human Rights\n"
                              "-------------------------------")
def firstSemBcomLlb(update:Update,context:CallbackContext):
    update.message.reply_text("Select your subject from below-\n"
                              "/1sub1Bllb Managerial Economics \n"
                              "-------------------------------\n"
                              "/2sub1Bllb Organizational Behaviour\n"
                              "-------------------------------\n"
                              "/3sub1Bllb Business Economics\n"
                              "-------------------------------\n"
                              "/4sub1Bllb Business Environment\n"
                              "-------------------------------\n"
                              "/5sub1Bllb Human Resource Development \n"
                              "-------------------------------\n"
                              "/6sub1Bllb General English")
def Managerial_Economics(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-managerial-economics-1-ns-3002-cv3-dec-2021.pdf")
def Organizational_Behaviour(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-organizational-behaviour-ns-3003-cv3-dec-2021.pdf")
def Business_Economics(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-business-environment-ns-3001-cv3-dec-2021.pdf")
def Business_Environment(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-business-environment-ns-3001-dec-2020.pdf")
def HRD(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-human-resource-development-ns-3004-nov-2019.pdf")
def general_english(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-1-sem-general-english-1-re-ns-3000-nov-2019.pdf")
def secondSemBcomLlb(update:Update,context:CallbackContext):
    update.message.reply_text("Select your subject from below-\n"
                              "/1sub2Bllb Business Management\n"
                              "-------------------------------\n"
                              "/2sub2Bllb Law of Torts and Consumer Protection\n"
                              "-------------------------------\n"
                              "/3sub2Bllb Managerial economics\n"
                              "-------------------------------\n"
                              "/4sub2Bllb Marketing management\n"
                              "-------------------------------\n"
                              "/5sub2Bllb Sales management \n")
def Business_Management(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-2-sem-business-management-ns-3008-jun-2022.pdf")
def LTCP(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-2-sem-law-of-torts-and-consumer-protection-act-ns-3010-jun-2022.pdf")
def Managerial_economics(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-2-sem-managerial-economics-ns-3006-jun-2022.pdf")
def Marketing_management(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-2-sem-marketing-management-ns-3009-jun-2022.pdf")
def Sales_management(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-2-sem-sales-management-ns-3007-jun-2022.pdf")
def CLOI(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-5-sem-constitutional-law-of-india-1-nature-of-the-constitution-ns-3023-cv3-dec-2021.pdf")
def SC(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-5-sem-contract-2-specific-contract-and-law-of-partnership-ns-3024-cv3-dec-2021.pdf")
def JLT (update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-5-sem-jurisprudence-1-legal-theory-ns-3025-cv3-dec-2021.pdf")
def LOC(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-5-sem-law-of-crimes-indian-penal-code-ns-3021-cv3-dec-2021.pdf")
def threeSemBcomLlb(update:Update,context:CallbackContext):
    update.message.reply_text("Select your subject from below-\n"
                              "/1sub3Bllb Consumer_Behaviour_Dec2021\n"
                              "-------------------------------\n"
                              "/2sub3Bllb General_Principle_Of_Contract_Dec2021\n"
                              "-------------------------------\n"
                              "/3sub3Bllb Entrepreneurship_Development_Dec2021\n"
                              "-------------------------------\n"
                              "/4sub3Bllb General_English_Dec2021\n"
                              "-------------------------------\n"
                              "/5sub3Bllb Indian_Legal_And_Constitutional_History_Dec2021\n")
def Consumer_Behaviour_Dec2021(update:Update,context:CallbackContext):
    update.message.reply_text("Year - 2021")
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-consumer-behaviour-ns-3013-cv3-dec-2021.pdf")
def General_English_Dec2021(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-general-english-2-ns-3011-c3-dec-2021.pdf")
def ILACH2021(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-indian-legal-and-constitutional-history-ns-3015-cv3-dec-2021.pdf")
def General_Principle_Of_Contract_Dec2021(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-contract-1-general-principles-of-contract-ns-3014-cv3-dec-2021.pdf")
def Entrepreneurship_Development_Dec2021(update:Update,context:CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-entrepreneurship-development-ns-3012-cv3-dec-2021.pdf")
##   update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-3-sem-contract-1-general-principles-of-contract-ns-3014-cv3-dec-2021.pdf")
def Auditing(update:Update,CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-4-sem-auditing-ns-3017-jun-2022.pdf")
def FAM(update:Update,CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-4-sem-financial-management-ns-3019-jun-2022.pdf")
def FCI(update:Update,CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-4-sem-fundamentals-of-computer-and-information-system-ns-3018-jun-2022.pdf")
def IM(update:Update,CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-4-sem-international-marketing-ns-3016-jun-2022.pdf")
def LOH(update:Update,CallbackContext):
    update.message.reply_text("https://www.ccsustudy.com/papers/bcomllb-4-sem-law-of-human-rights-ns-3020-jun-2022.pdf")
def bca(update:Update,CallbackContext):
    update.message.reply_text("Please select your Semester-\n"
                              "/1st_SEM_Bca\n"
                              "/2nd_SEM_Bca\n"
                              "/3rd_SEM_Bca\n"
                              "/4th_SEM_Bca\n"
                              "/5th_SEM_Bca\n"
                              "/6th_SEM_Bca\n")

def firstSemBCA(update:Update,CallbackContext):
    update.message.reply_text("PPA\n"
                              "https://www.ccsustudy.com/papers/bca-1-sem-programming-principles-and-algorithm-18002-cv-3-dec-2021.pdf\n"
                                                            "-------------------------------\n"

                              "CFOA\n"
                              "https://www.ccsustudy.com/papers/bca-1-sem-computer-fundamentals-and-office-automation-18001-cv3-dec-2021.pdf\n"
                                                            "-------------------------------\n"

                              "POM\n"
                              "https://www.ccsustudy.com/papers/bca-1-sem-principles-of-management-18003-cv3-dec-2021.pdf\n"
                              "-------------------------------\n"

                              "BC\n"
                              "https://www.ccsustudy.com/papers/bca-1-sem-business-communication-18004-cv2-nov-2021.html#google_vignette\n"
                              "-------------------------------\n"

                              "EVS\n"
                              "https://www.ccsustudy.com/papers/bba-bca-bpt-etc-environmental-studies-np-3440-cv2-nov-2021.pdf")

def sixthSemBCA(update:Update,CallbackContext):
    update.message.reply_text("")
def secondSemBCA(update:Update,CallbackContext):
    update.message.reply_text("")
def thirdSemBCA(update:Update,CallbackContext):
    update.message.reply_text("")
def forthSemBCA(update:Update,CallbackContext):
    update.message.reply_text("")
def fifthSemBCA(update:Update,CallbackContext):
    update.message.reply_text("")
updater.dispatcher.add_handler(CommandHandler('start',startFun))
updater.dispatcher.add_handler(CommandHandler('ccsu', ccsuMenu))
updater.dispatcher.add_handler(CommandHandler('BCOM_LLB',bcomLLB))
updater.dispatcher.add_handler(CommandHandler('BCOM',bcom))
updater.dispatcher.add_handler(CommandHandler('BCA',bca))
updater.dispatcher.add_handler(CommandHandler('1st_SEM_Bca',firstSemBCA))
updater.dispatcher.add_handler(CommandHandler('2nd_SEM_Bca',secondSemBCA))
updater.dispatcher.add_handler(CommandHandler('3rd_SEM_Bca',thirdSemBCA))
updater.dispatcher.add_handler(CommandHandler('4th_SEM_Bca',forthSemBCA))
updater.dispatcher.add_handler(CommandHandler('5th_SEM_Bca',fifthSemBCA))
updater.dispatcher.add_handler(CommandHandler('6th_SEM_Bca',sixthSemBCA))
updater.dispatcher.add_handler(CommandHandler('1st_SEM_Bcom',firstSemBcom))
updater.dispatcher.add_handler(CommandHandler('2nd_SEM_Bcom',secondSemBcom))
updater.dispatcher.add_handler(CommandHandler('1st_SEM_BcomLLB',firstSemBcomLlb))
updater.dispatcher.add_handler(CommandHandler('1sub1Bllb',Managerial_Economics))
updater.dispatcher.add_handler(CommandHandler('2sub1Bllb',Organizational_Behaviour))
updater.dispatcher.add_handler(CommandHandler('3sub1Bllb',Business_Economics))
updater.dispatcher.add_handler(CommandHandler('4sub1Bllb',Business_Environment))
updater.dispatcher.add_handler(CommandHandler('5sub1Bllb',HRD))
updater.dispatcher.add_handler(CommandHandler('6sub1Bllb',general_english))
updater.dispatcher.add_handler(CommandHandler('2nd_SEM_BcomLLB',secondSemBcomLlb))
updater.dispatcher.add_handler(CommandHandler('1sub2Bllb',Business_Management))
updater.dispatcher.add_handler(CommandHandler('2sub2Bllb',LTCP))
updater.dispatcher.add_handler(CommandHandler('3sub2Bllb',Managerial_economics))
updater.dispatcher.add_handler(CommandHandler('4sub2Bllb',Marketing_management))
updater.dispatcher.add_handler(CommandHandler('5sub2Bllb',Sales_management))
updater.dispatcher.add_handler(CommandHandler('3rd_SEM_BcomLLB',threeSemBcomLlb))
updater.dispatcher.add_handler(CommandHandler('1sub3Bllb',Consumer_Behaviour_Dec2021))
updater.dispatcher.add_handler(CommandHandler('2sub3Bllb',General_Principle_Of_Contract_Dec2021))
updater.dispatcher.add_handler(CommandHandler('4sub3Bllb',General_English_Dec2021))
updater.dispatcher.add_handler(CommandHandler('3sub3Bllb',Entrepreneurship_Development_Dec2021))
updater.dispatcher.add_handler(CommandHandler('5sub3Bllb',ILACH2021))
updater.dispatcher.add_handler(CommandHandler('4th_SEM_BcomLLB',forthSemBcomLlb))
updater.dispatcher.add_handler(CommandHandler('1sub4Bllb',Auditing))
updater.dispatcher.add_handler(CommandHandler('2sub4Bllb',FAM))
updater.dispatcher.add_handler(CommandHandler('3sub4Bllb',FCI))
updater.dispatcher.add_handler(CommandHandler('4sub4Bllb',IM))
updater.dispatcher.add_handler(CommandHandler('5sub4Bllb',LOH))
updater.dispatcher.add_handler(CommandHandler('5th_SEM_BcomLLB',fifthSemBcomLlb))
updater.dispatcher.add_handler(CommandHandler('1sub5Bllb',CLOI))
updater.dispatcher.add_handler(CommandHandler('2sub5Bllb',SC))
updater.dispatcher.add_handler(CommandHandler('3sub5Bllb',JLT))
updater.dispatcher.add_handler(CommandHandler('4sub5Bllb',LOC))


#updater.dispatcher.add_handler(CommandHandler('2_General_Principle_Of_Contract_Dupdater.dispatcher.add_handler(CommandHandler('4th_SEM_BcomLLB',forthSemBcomLlb))ec2021',PrincipleContract_Dec2021))
updater.start_polling()
print("run")
