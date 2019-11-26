import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

    #       STEPS:
    #       1) Read file Test.xml
    #       2) Insert informations about tests in arrays  
    #             a = np.array([[1, 2], [3, 4]])
    #             b = np.array([[5, 6]])
    #             np.concatenate((a, b.T), axis=1) 
    #             array([[1, 2, 5],
    #                   [3, 4, 6]])
    #       3) Constructing DataFrame from numpy ndarray:
    #             df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    #                                                     columns=['a', 'b', 'c'])
    #             a  b  c
    #             0  1  2  3
    #             1  4  5  6
    #             2  7  8  9
    #       4) Insert dataframe into csv file (maybe my axis is wrong)
    #             df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
    #                                'mask': ['red', 'purple'],
    #                                'weapon': ['sai', 'bo staff']})
    #             df.to_csv(index=False)


if __name__ == "__main__":

    # __________ CHANGE HERE YOUR FILE NAME __________ #

    fileName = 'ServiceTests'

    # ________________________________________________ #

    # _____STEP 1_____ #
    tree = ET.parse( str(fileName) + '.xml')
    root = tree.getroot()

    idArray = np.array([])
    testNameArray = np.array([])
    classNameArray = np.array([])
    timeArray = np.array([])
    resultArray = np.array([])

    n_testCase = 1
    testStatus = None
    for testCase in root.iter('testcase'):

        # __NEEDS FOR DEBUGGING__ #
        # print('\n')
        # print(' id ' + str(n_testCase))
        # print(' testName ' + str(testCase.attrib['name']))
        # print(' className ' + str(testCase.attrib['classname']))
        # print(' time ' + str(testCase.attrib['time']))

        if( 'ignored' in testCase.attrib ):
            testStatus = 'ignored'
        else:
            testStatus = 'passed'
        
        # _____STEP 2_____ #
        idArray = np.append( idArray, np.array([str(n_testCase)]) ) 
        testNameArray = np.append( testNameArray, np.array(str(testCase.attrib['name'])) )
        classNameArray = np.append( classNameArray, np.array(str(testCase.attrib['classname'])) )
        timeArray = np.append( timeArray, np.array(str(testCase.attrib['time'])) )
        resultArray = np.append( resultArray, np.array(testStatus))

        n_testCase = n_testCase + 1

    # _____TEST 3_____ #
    finalDataframe = pd.DataFrame(  np.array([  idArray, 
                                                testNameArray, 
                                                classNameArray, 
                                                timeArray, 
                                                resultArray]).T ,
                                            columns=[
                                                'Count', 
                                                'Test name', 
                                                'Class name', 
                                                'Time', 
                                                'Result'])

    # _____STEP______ 4 #
    f= open(fileName + '.csv',"w+")
    finalDataframe.to_csv( fileName + '.csv' ,index=False)
    f.close



    # __NEEDS FOR FUTURE DEBUGGING__ #
    # print(idArray)
    # print(testNameArray)
    # print(classNameArray)
    # print(timeArray)
    # print(resultArray)
    # if( idArray.size == testNameArray.size == classNameArray.size == timeArray.size == resultArray.size ):
    #     print(" LA SIZE DEGLI ARRAY E' CORRETTA")
