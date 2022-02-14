# import sys
numOfBuildings = 0;
roads = [];
buildingCostRent = [];
val = 6;#int(input());#sys.stdin.readline();
numOfBuildings = val;
# for i in range(numOfBuildings-1):
#     roads.append(list(map(int, input().split(" "))));
#
# for i in range(numOfBuildings):
#     buildingCostRent.append(list(map(int, input().split(" "))));

buildings = [];
buildingRoads = [];
roads = [[2,1,17],[1,3,5],[3,4,3],[5,3,6],[5,6,10]];
buildingCostRent = [[3,1],[2,0],[1,9],[4,3],[3,5],[4,4]];

for i in range(numOfBuildings):
    buildings.append({'buildingIndex':i+1,'cost':buildingCostRent[i][0],'rent':buildingCostRent[i][1],'roads':[]})

for road in roads:
    buildings[road[0]-1]['roads'].append([road[1], road[2], buildings[road[0]-1]['cost']*road[2]+buildings[road[0]-1]['rent']]);
    buildings[road[1]-1]['roads'].append([road[0], road[2], buildings[road[1]-1]['cost']*road[2]+buildings[road[1]-1]['rent']]);

# print(buildings);
for i in buildings:
    print(i);
#back tracking algo
def costToTravelPerBuilding(frombd, tobd, vehicleCost=None, vehicleRent=None, sourcebd=None):
    print(str(frombd) + "-" + str(tobd) + "-" + str(sourcebd) + "-" + str(vehicleCost) + "-" + str(vehicleRent));
    #1 => 4
    fromBuilding = buildings[frombd-1];
    for road in fromBuilding['roads']:
        # to find if there is a direct road
        if tobd == road[0]:
            # return {vehicleCost: fromBuilding['cost'], vehicleRent: fromBuilding['rent'], overallcost: road[2], distance:road[1]};#cost
            return {'overallcost': road[2], 'distance':road[1]};#cost

    for road in fromBuilding['roads']:
        if road[0] == sourcebd:
            continue;

        print("road exploration");
        print("Road - " + str(road[0]) + "-" + str(tobd));
        foundRoad = costToTravelPerBuilding(road[0], tobd, fromBuilding['cost'], fromBuilding['rent'], frombd);
        if foundRoad is None:
            continue;

        print("Road found!");
        print(fromBuilding);
        print(foundRoad);
        cost = fromBuilding['cost'] * road[1] + fromBuilding['rent'];
        print(fromBuilding);
        print(cost);
        if foundRoad['overallcost'] > (fromBuilding['cost'] * foundRoad['distance']):
            #use the same vehicle to travel
            print("2 - " + str(fromBuilding['cost'] * foundRoad['distance']));
            cost += fromBuilding['cost'] * foundRoad['distance'];

            # return {vehicleCost: fromBuilding['cost'], vehicleRent: fromBuilding['rent'], overallcost: road[2], distance:road[1]};#cost
            return {'overallcost': cost, 'distance':road[1]};#cost
        else:
            print("3 - " + str(foundRoad['overallcost']));
            cost += foundRoad['overallcost'];

            # return {vehicleCost: fromBuilding['cost'], vehicleRent: fromBuilding['rent'], overallcost: road[2], distance:road[1]};#cost
            return {'overallcost': cost, 'distance':road[1]};#cost

    return None;

print(costToTravelPerBuilding(1, 6, None, None, None))
minimalCostReqdToTravel = [];
# for i in range(2, numOfBuildings+1):
#     # print('Building - ' + str(i));
#     data = costToTravelPerBuilding(1, i, None, None, None);
#     # print(data);
#     minimalCostReqdToTravel.append(data['overallcost']);

# print(*minimalCostReqdToTravel);
print(minimalCostReqdToTravel);
