package cmp4008y_cw1;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Collections;
// reference: https://www.w3schools.com/java/java_arraylist.asp

public class MessierCatalogue {
    private List <MessierObject> objects;

    // creating new array list
    public MessierCatalogue() {
        objects = new ArrayList<>();
    }

    //adding items to the list
    public void addObject(MessierObject object) {
        objects.add(object);
    }

    // gets the messier number from messierObject()
    public MessierObject getByMessierNumber(String number) {
        for (MessierObject object : objects) {
            if (object.getMessierNumber().equals(number)) { // if a value is present, return object and add it to the list
                return object;
            }
        }
        return null;
    }

    // searches messierObject for catalogue number
    public MessierObject getByCatalogueNumber(String ngc) {
        for (MessierObject object : objects) {
            if (object.getNGCNumber().equals(ngc)) {
                return object;
            }
        }
        return null;
    }

    // gets type from messierObject and adds them to new arraylist results
    public List <MessierObject> getByType(String type) {
        List <MessierObject> result = new ArrayList<>();
        for (MessierObject object : objects) {
            if (object.getType().equalsIgnoreCase(type)) {
                result.add(object);
            }
        }
        return result;
    }

    public List <MessierObject> getByConstellation(String constellation) {
        List <MessierObject> result = new ArrayList<>();
        for (MessierObject object : objects) {
            if (object.getConstellation().equals(constellation)) {
                result.add(object);
            }
        }
        return result;
    }

    public List <MessierObject> getBrightestObjects() {
        List <MessierObject> sorted = new ArrayList<>(objects);
        Collections.sort(sorted);
        return sorted;
        // reference: https://www.w3schools.com/java/java_collections.asp
        //            https://www.geeksforgeeks.org/java/arrays-sort-in-java/
    }

    public List <MessierObject> sortByConstellation() {
        List <MessierObject> sorted = new ArrayList<>(objects);
        Collections.sort(sorted, new Comparator<MessierObject>() {
            @Override
            public int compare(MessierObject o1, MessierObject o2) {
                return o1.getConstellation().compareTo(o2.getConstellation());
            }
        });
        return sorted;
    }

    public double getAverageMagnitude(String type) {
        List <MessierObject> objectsOfType = getByType(type);
        if (objectsOfType.isEmpty()) {
            return 0;
        }
        double sum = 0;
        for (MessierObject object : objectsOfType) {
            sum += object.getApparentMagnitude();
        }
        return sum / objectsOfType.size();
    // reference: https://www.w3schools.com/java/ref_string_isempty.asp
    }

    public MessierObject getLeastDistance(String type) {
        List <MessierObject> objectsOfType = getByType(type);
        if (objectsOfType.isEmpty()) {
            return null;
        }
        MessierObject leastDistance = objectsOfType.get(0);
        for (MessierObject object : objectsOfType) {
            if (object.getDistanceKLY() < leastDistance.getDistanceKLY()) {
                leastDistance = object;
            }
        }
        return leastDistance;
    }

    public MessierObject getMostDistance(String constellation) {
        List <MessierObject> objectsInConstellation = getByConstellation(constellation);
        if (objectsInConstellation.isEmpty()) {
            return null;
        }
        MessierObject mostDistance = objectsInConstellation.get(0);
        for (MessierObject object : objectsInConstellation) {
            if (object.getDistanceKLY() < mostDistance.getDistanceKLY()) {
                mostDistance = object;
            }
        }
        return mostDistance;
    }

    public MessierObject getClosestObject(MessierObject target) {
        if (objects.size() <= 1) {
            return null;
        }
        MessierObject closets = null;
        double closestDistance = Double.MAX_VALUE;
        for (MessierObject object : objects) {
            if (object == target || object.getMessierNumber().equals(target.getMessierNumber())) {
                continue;
            }
            double distance = getAngularDistance(target, object);
            if (distance < closestDistance) {
                closestDistance = distance;
                closets = object;
            }
        }
        return closets;
    }

    // calculate angular distance
    public double getAngularDistance(MessierObject object1, MessierObject object2) {
        double RA_1 = object1.getRightAscension();
        double RA_2 = object2.getRightAscension();
        double DEC_1 = object1.getDeclination();
        double DEC_2 = object2.getDeclination();
        double deltaRA = RA_2 - RA_1;
        double cosAngle = Math.sin(DEC_1) * Math.sin(DEC_2)  + Math.cos(DEC_1) * Math.cos(DEC_2) * Math.cos(deltaRA);
        return Math.acos(cosAngle);
        // reference: https://stjerneskinn.com/angular-distance-between-stars.htm
        //            https://www.w3schools.com/java/ref_math_cos.asp
    }

    //method to convert any ints to strings for display
    @Override
    public String toString() {
        String result = "";
        for (MessierObject object : objects) {
            result += object.toString() + "\n";
        }
        return result;
    }
}
