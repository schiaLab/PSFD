import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def timeSeriesEmbedding(series:np.array, dim):

    aList = []

    for n in range(len(series)-dim+1):

        aList.append(series[n:(n+dim)])


    return np.array(aList)


def correlationIntegral(embeddedSpace:np.array, r):

    N = embeddedSpace.shape[1]

    sum = 0

    for n in range(N):

        for n2 in range(N):


            if n == n2:

                continue

            else:

                deltaX = np.linalg.norm(embeddedSpace[:, n] - embeddedSpace[:, n2], ord=None, axis=None, keepdims=False)

                if r - deltaX > 0:

                    sum += 1

                else:

                    continue


    return sum / (N ** 2)


def dimensionEstimate(embeddedSpace:np.array, start=1.001, end=2, num=50, plot=False):

    num = num+1

    rList = np.linspace(start, end, num)

    cList= [correlationIntegral(embeddedSpace, r) for r in rList]

    cList = np.array(cList)

    cList = np.log(cList)

    rList = np.log(rList)

    if plot :
        sns.set()
        sns.regplot(x=rList, y=cList)
        plt.title("Threshold-Correlation Integral Log Relation")
        plt.show()

    cListBar = np.mean(cList)
    rBar = np.mean(rList)



    slope = np.sum((cList - cListBar) * (rList - rBar)) / np.sum((rList - rBar)**2)

    b = cListBar - (slope * rBar)

    estiList = [((slope * r) + b) for r in rList]

    estiList = np.array(estiList)


    loss = np.mean(np.abs(cList - estiList))



    print("Fractal Dimension: %f"%slope)
    print("Loss: %f" % loss)

    return slope, loss


'''
def embeddingDimensionEstimate(series, maxDim, featureNum):

    dimDict = {}
    dimListDict = {}
    psfdList = []
    embeddingDimDict = {}

    for dim in range(maxDim):

        if dim == 1 or dim == 0:

            continue

        else:

            phaseSpace = timeSeriesEmbedding(series, dim + 1)

            PSFD, loss , dimList = dimensionEstimate(phaseSpace, num=featureNum)

            psfdList.append(PSFD)

            dimDict[PSFD] = loss

            embeddingDimDict[PSFD] = dim+1

            dimListDict[PSFD] = dimList

    leastLossDim = min(dimDict, key=dimDict.get)

    print("Dimension of Least Loss: %f"%leastLossDim)
    print("Embedding Dimension of Least Loss: %f" %embeddingDimDict[leastLossDim])

    return dimListDict[leastLossDim], psfdList


def psfdPatternExtraction(dataFrame:pd.DataFrame, maxDim, featureNum):

    result = []

    result2 = []

    for n in range(dataFrame.shape[0]):

        subResult, subResult2 = embeddingDimensionEstimate(dataFrame.iloc[n, :].values, maxDim, featureNum)

        result.append(subResult)

        result2.append(subResult2)


    return {"moving r value":pd.DataFrame(result), "moving edembedding space":pd.DataFrame(result2)}


'''