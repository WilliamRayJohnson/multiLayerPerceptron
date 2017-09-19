import Net

def main():
    perceptron = Net.Net(1, 2, 1, 0.5)
    trainingData = [([-1.0],[2.0]),([-0.9],[1.81]),([-0.8],[1.64]),([-0.7],[1.49]),([-0.6],[1.35]),
        ([-0.5],[1.25]),([-0.4],[1.16]),([-0.3],[1.09]),([-0.2],[1.04]),([-0.1],[1.01]),([0.0],[1.0]),
        ([0.1],[1.01]),([0.2],[1.04]),([0.3],[1.09]),([0.4],[1.16]),([0.5],[1.25]),([0.6],[1.35]),
        ([0.7],[1.49]),([0.8],[1.64]),([0.9],[1.81]),([1.0],[2.0])]
        
    perceptron.train(trainingData)
    
    
if __name__ == '__main__':
    main()