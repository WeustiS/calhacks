import torch.nn.utils.prune as prune
from baseline import *
from modules import *
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

r0 = torch.rand(1, 3, 1080, 720).to(device)

def measure(model, r):
    arr = [0] * 9
    for i in range(25):
        model(r)
    for i in range(10):
        arr = [sum(x) for x in zip(arr, model(r))]
    return sum(arr)


model = Baseline().to(device)

print("Unpruned time", measure(model, r0), "\n")

parameters_to_prune = (
    (model.conv1.conv, 'weight'),
    (model.conv1.conv, 'bias'),
    (model.conv2.conv, 'weight'),
    (model.conv2.conv, 'bias'),
    (model.conv3.conv, 'weight'),
    (model.conv3.conv, 'bias'),
    (model.deconv2.deconv, 'weight'),
    (model.deconv2.deconv, 'bias'),
    (model.deconv3.deconv, 'weight'),
    (model.deconv3.deconv, 'bias'),
    (model.deconv4.deconv, 'weight'),
    (model.deconv4.deconv, 'bias'),
)

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.20,
)
print("Pruned time: 20", measure(model, r0))
print()

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.25,
)
print("Pruned time: 25", measure(model, r0))
print()

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.33,
)
print("Pruned time: 33", measure(model, r0))
print()

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.5,
)
print("Pruned time: 50", measure(model, r0))
print()

prune.global_unstructured(
    parameters_to_prune,
    pruning_method=prune.L1Unstructured,
    amount=0.75,
)
print("Pruned time: 75", measure(model, r0))
print()