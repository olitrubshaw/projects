package cmp4008y_cw1;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.List;
import java.util.Scanner;

public class MessierProgram {
    public static void main(String[] args) {
        MessierCatalogue catalogue = loadCatalogue("messier.txt");
        if (catalogue == null) {
            System.out.println("no catalogue file found");
            return;
        }
        System.out.println("catalogue loaded");
        displayCatalogueConstellation(catalogue);
        displayAverageGlobalClusterMagnitude(catalogue);
        displayLeastDistantOpenCluster(catalogue);
        displayHighestDeclinationSagittarius(catalogue);
        displayClosestObjectM45(catalogue);
    }
    private static MessierCatalogue loadCatalogue(String filename) {
        MessierCatalogue catalogue = new MessierCatalogue();
        try {
            File file = new File(filename);
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                MessierObject object = new MessierObject(line);
                catalogue.addObject(object);
            }
            scanner.close();
            return catalogue;
    }
        catch (FileNotFoundException e) {
        System.out.println("file not found");
        return null;
        }
    }

    private static void displayCatalogueConstellation(MessierCatalogue catalogue) {
        System.out.println("a.) catalogue order sorted by constellation");
        List <MessierObject> sorted = catalogue.sortByConstellation();
        for (MessierObject object : sorted) {
            System.out.println(object.toString());
        }
        System.out.println();
    }

    private static void displayAverageGlobalClusterMagnitude(MessierCatalogue catalogue) {
        System.out.println("b.) average apparent magnitude of all globular clusters");
        double average = catalogue.getAverageMagnitude("globular cluster");
        System.out.println("average apparent magnitude: " + average);
        System.out.println();
    }

    private static void displayLeastDistantOpenCluster(MessierCatalogue catalogue) {
        System.out.println("c.) least distant open cluster");
        MessierObject closest = catalogue.getLeastDistance("open cluster");
        if (closest != null) {
            System.out.println(closest.toString());
        }
        else {
            System.out.println("no open cluster found");
        }
        System.out.println();
    }

    private static void displayHighestDeclinationSagittarius(MessierCatalogue catalogue) {
        System.out.println("d.) highest declination object in sagittarius");
        MessierObject highest = null;
        List<MessierObject> sag = catalogue.getByConstellation("Sagittarius");
        for (MessierObject object : sag) {
            if (highest == null || object.getDeclination() > highest.getDeclination()) {
                highest = object;
            }
        }
        if (highest != null) {
            System.out.println(highest.toString());
        }
        else {
            System.out.println("no highest declination sagittarius found");
        }
        System.out.println();
    }

    private static void displayClosestObjectM45(MessierCatalogue catalogue) {
        System.out.println("e.) closest object to m45");
        MessierObject m45 = catalogue.getByMessierNumber("M45");
        if (m45 == null) {
            System.out.println("cannot find M45");
            return;
        }
        MessierObject closest = catalogue.getClosestObject(m45);
        if (closest != null) {
            double distance = catalogue.getAngularDistance(m45, closest);
            System.out.println(closest.toString());
            System.out.println("angular distance: " + Math.toDegrees(distance) + " degrees");
        }
        else {
            System.out.println("no object found");
        }
        System.out.println();
    }
}
// reference: https://www.w3schools.com/java/ref_scanner_nextline.asp
//            https://www.geeksforgeeks.org/java/stack-addobject-method-in-java-with-example/
