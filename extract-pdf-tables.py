#!/usr/bin/python3
#
# Doc 242   f73381b3-95a8-4c48-a227-60191de51a7b.pdf
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI INC. (CASE NO. 22-19361)
# 51-11015  Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# Doc 243   e4f2e8a4-4640-4fcd-bb70-30721e0e6008.pdf
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI INC. (CASE NO. 22-19361)
# 225-5389  SOFA Part 2, Question 3 ‐ Payments or transfers made to creditors within 90 days preceding commencement of this case
#
# Doc 247   527a71cf-4aa7-48ab-a646-228e5265657a.pdf
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI INTERNATIONAL LTD. (CASE NO. 22-19368)
# 48-4813   Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# Doc 248   b49c389d-5061-4990-b533-435db20a6cb1.pdf
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI INTERNATIONAL LTD. (CASE NO. 22-19368)
# 42-550    SOFA Part 2, Question 3 ‐ Payments or transfers made to creditors within 90 days preceding commencement of this case
# 551-2453  SOFA Part 11, Question 21 ‐ Property held for another
#
# Doc 249   6b093f33-94cb-4fef-9320-ccb24fae6e88
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI INVESTMENT PRODUCTS LLC (CASE NO. 22-19370)
#
# Dco 250   eca42c12-5139-44c3-be18-52156ec32922
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI INVESTMENT PRODUCTS LLC (CASE NO. 22-19370)
#
# Doc 251   6e261a4e-fa03-495b-ab9f-1c7bf0a6c807
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI LENDING LLC (CASE NO. 22-19365)
# 48-105    Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# Doc 252   7d2548d4-cf38-4c95-9552-96611260858d
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI LENDING LLC (CASE NO. 22-19365)
# 61-107    SOFA Part 2, Question 3 ‐ Payments or transfers made to creditors within 90 days preceding commencement of this case
#
# Doc 253   ee93b6f4-0463-40d7-a32c-14378d9aeea0
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI LENDING II LLC (CASE NO. 22-19374)
#
# Doc 254   3e0df730-e3da-48cc-8d20-9b9b312b5555
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI LENDING II LLC (CASE NO. 22-19374)
#
# Doc 255   65ca239f-520a-446b-9321-5543e141f8db
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI SERVICES INC. (CASE NO. 22-19371)
#
# Doc 256   e548f4b3-cd72-423a-a126-a393a072372d
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI SERVICES INC. (CASE NO. 22-19371)
# 43-45     SOFA Part 2, Question 3 ‐ Payments or transfers made to creditors within 90 days preceding commencement of this case
#
# Doc 257   cab6560a-fd87-4d0e-bea5-93115287168a
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI TRADING LLC (CASE NO. 22-19363)
#
# Doc 258   b91d53cb-efec-426a-b3c6-cfda75d501ba
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI TRADING LLC (CASE NO. 22-19363)
#
# Doc 259   00060102-eda5-4285-8d74-656fb888862e
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI VENTURES LLC (CASE NO. 22-19367)
#
# Doc 260   7529ca6d-e3d7-4ac4-881c-5fe2baccea10
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI VENTURES LLC (CASE NO. 22-19367)
#
# Doc 261   8ac683ac-5b91-479e-b103-c781fe121198
#           SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI WALLET LLC (CASE NO. 22-19366)
#
# Doc 262   5feafc85-f9ad-43fc-8c72-aa07b04f3b0e
#           STATEMENT OF FINANCIAL AFFAIRS FOR BLOCKFI WALLET LLC (CASE NO. 22-19366)
# 129-841   SOFA Part 2, Question 3 ‐ Payments or transfers made to creditors within 90 days preceding commencement of this case
# 842-6675  SOFA Part 11, Question 21 ‐ Property held for another
#
# Doc 460   3494cb80-38d0-4d12-a26f-da9b1064d5a0
#           AMENDED SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI INC. (CASE NO. 22-19361)
# 6         Amended Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# Doc 461   a9f803bf-f625-40ca-87c4-6025eff39bf4
#           AMENDED SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI LENDING LLC (CASE NO. 22-19365)
# 4         Amended Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# Doc 462   12809980-d45f-4399-a3cd-e0fdba7799ce
#           AMENDED SCHEDULE OF ASSETS AND LIABILITIES FOR BLOCKFI INTERNATIONAL LTD. (CASE NO. 22-19368)
# 4-35      Amended Schedule E/F: Part 2 ‐ Creditors With Nonpriority Unsecured Claims
#
# #

import camelot
import threading
import time

from multiprocessing import Process

import timeit
start = 0
stop = 0
d242 = {"inputfile": "pdf/f73381b3-95a8-4c48-a227-60191de51a7b.pdf",
        "outputfile": "output-stage1/242-blockfiinc-unsecuredclaims", "startpage": 51, "endpage": 11015}
d243 = {"inputfile": "pdf/e4f2e8a4-4640-4fcd-bb70-30721e0e6008.pdf",
        "outputfile": "output-stage1/243-blockfiinc-90daypayments", "startpage": 225, "endpage": 5389}
d247 = {"inputfile": "pdf/527a71cf-4aa7-48ab-a646-228e5265657a.pdf",
        "outputfile": "output-stage1/247-blockfiintl-unsecuredclaims", "startpage": 48, "endpage": 4813}
d248a = {"inputfile": "pdf/b49c389d-5061-4990-b533-435db20a6cb1.pdf",
         "outputfile": "output-stage1/248-blockfiintl-90daypayments", "startpage": 42, "endpage": 550}
d248b = {"inputfile": "pdf/b49c389d-5061-4990-b533-435db20a6cb1.pdf",
         "outputfile": "output-stage1/248-blockfiintl-propertyheld", "startpage": 551, "endpage": 2453}
d251 = {"inputfile": "pdf/6e261a4e-fa03-495b-ab9f-1c7bf0a6c807.pdf",
        "outputfile": "output-stage1/251-lendingllc-unsecuredclaims", "startpage": 48, "endpage": 105}
d252 = {"inputfile": "pdf/7d2548d4-cf38-4c95-9552-96611260858d.pdf",
        "outputfile": "output-stage1/252-lendingllc-90daypayments", "startpage": 61, "endpage": 107}
d256 = {"inputfile": "pdf/e548f4b3-cd72-423a-a126-a393a072372d.pdf",
        "outputfile": "output-stage1/256-servicesinc-90daypayments", "startpage": 43, "endpage": 45}
d262a = {"inputfile": "pdf/5feafc85-f9ad-43fc-8c72-aa07b04f3b0e.pdf",
         "outputfile": "output-stage1/262-walletllc-90daypayments", "startpage": 129, "endpage": 841}
d262b = {"inputfile": "pdf/5feafc85-f9ad-43fc-8c72-aa07b04f3b0e.pdf",
         "outputfile": "output-stage1/262-walletllc-propertyheld", "startpage": 842, "endpage": 6675}
d461 = {"inputfile": "pdf/a9f803bf-f625-40ca-87c4-6025eff39bf4.pdf",
        "outputfile": "output-stage1/461-lendingllc-unsecuredclaims", "startpage": 4, "endpage": 4}
d462 = {"inputfile": "pdf/12809980-d45f-4399-a3cd-e0fdba7799ce.pdf",
        "outputfile": "output-stage1/462-blockfiintl-unsecuredclaims", "startpage": 4, "endpage": 35}
# d = {"inputfile": "pdf/.pdf", "outputfile": "output/", "startpage": , "endpage": }
dcoins = {"inputfile": "pdf/b49c389d-5061-4990-b533-435db20a6cb1.pdf",
          "outputfile": "output-stage1/dcoins", "startpage": 14, "endpage": 16}
d242tf = {"inputfile": "pdf/f73381b3-95a8-4c48-a227-60191de51a7b.pdf",
        "outputfile": "output-stage1/242-blockfiinc-unsecuredclaims", "startpage": 9983, "endpage": 9983}


def tstart():
    global start
    start = timeit.default_timer()


def tend():
    global stop
    stop = timeit.default_timer()
    execution_time = stop - start
    print("Program Executed in "+str(round(execution_time, 4)), " seconds")


def getTables2(start, end, increment, inputfile, outputfile, mode='lattice',split_text=True):
    striptext = ('\n')
    for x in range(start, end+1, increment):
        print("working on page " + str(x))
        # for the 90 day payments, split_text=True needs added to read_pdf
        tables = camelot.read_pdf(inputfile, 
            pages=str(x), flavor=mode, 
            strip_text=striptext, split_text=split_text)
        tables.export(outputfile, f='csv')


def getgeneric(dd, mode='lattice',split_text=True):
    inputfile = dd['inputfile']
    outputfile = dd['outputfile']
    sp = dd['startpage']
    ep = dd['endpage']
    tc = 8

    p1 = Process(target=getTables2, args=(
        sp, ep, tc, inputfile, outputfile, mode, split_text))
    p2 = Process(target=getTables2, args=(
        sp+1, ep, tc, inputfile, outputfile, mode, split_text))
    p3 = Process(target=getTables2, args=(
        sp+2, ep, tc, inputfile, outputfile, mode, split_text))
    p4 = Process(target=getTables2, args=(
        sp+3, ep, tc, inputfile, outputfile, mode, split_text))
    p5 = Process(target=getTables2, args=(
        sp+4, ep, tc, inputfile, outputfile, mode, split_text))
    p6 = Process(target=getTables2, args=(
        sp+5, ep, tc, inputfile, outputfile, mode, split_text))
    p7 = Process(target=getTables2, args=(
        sp+6, ep, tc, inputfile, outputfile, mode, split_text))
    p8 = Process(target=getTables2, args=(
        sp+7, ep, tc, inputfile, outputfile, mode, split_text))
    tstart()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    tend()


if __name__ == "__main__":
    getgeneric(d242, split_text=False)  #unsecuredclaims
    getgeneric(d243)
    getgeneric(d247)  #unsecuredclaims
    getgeneric(d248a)
    getgeneric(d248b)   #propertyheld
    getgeneric(d251)  #unsecuredclaims
    getgeneric(d252)
    getgeneric(d256)
    getgeneric(d262a)
    getgeneric(d262b) #propertyheld
    getgeneric(d461)  #unsecuredclaims
    getgeneric(d462, split_text=False)  #unsecuredclaims
    getgeneric(dcoins)
    #getgeneric(d242tf)
