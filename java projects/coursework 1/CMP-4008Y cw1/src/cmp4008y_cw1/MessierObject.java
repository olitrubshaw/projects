package cmp4008y_cw1;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MessierObject implements Comparable<MessierObject> {
    //create variables for all instances needed for messierObject
    private String messierNumber;
    private String ngcNumber;
    private String objectName;
    private String type;
    private String constellation;
    private double distanceKLY;
    private double apparentMagnitude;
    private double rightAscension;
    private double declination;
    private String ogRA;
    private String ogDEC;

    //constructor for messierObject
    public MessierObject(String line) {
        String[] fields = parseCSV(line); // splits the txt content into 9 parts
        for (int i = 0; i < fields.length; i++) { // removes white spaces from the txt content
            fields[i] = fields[i].trim();
        }

        //initialise variables by linking to the txt content
        this.messierNumber = fields[0];
        this.ngcNumber = removeQuotes(fields[1]);
        this.objectName = removeQuotes(fields[2]);
        this.type = fields[3];
        String distanceText =  fields[4];
        if (distanceText.contains("-")) {
            distanceText = distanceText.substring(0, distanceText.indexOf("-"));
        }
        this.distanceKLY = Double.parseDouble(distanceText.trim()); // returns a double value from the string
        this.constellation = fields[5];
        this.apparentMagnitude = Double.parseDouble(fields[6]);
        this.ogRA = fields[7];
        this.ogDEC = fields[8];
        this.rightAscension = convertRA(ogRA); // converts the right ascension into radians
        this.declination = convertDEC(ogDEC);
    }

    // csv parse fix
    private String[] parseCSV(String line) {
        List<String> fields = new ArrayList<>();
        boolean inQuotes = false;
        StringBuilder currentField = new StringBuilder();
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == '"') {
                inQuotes = !inQuotes;
                currentField.append(c);
            }
            else if (c == ',' && !inQuotes) {
                fields.add(currentField.toString());
                currentField = new StringBuilder();
            }
            else {
                currentField.append(c);
            }
        }
        fields.add(currentField.toString());
        return fields.toArray(new String[0]);
        // reference: https://stackoverflow.com/questions/1757065/java-splitting-a-comma-separated-string-but-ignoring-commas-in-quotes
    }

    // removes quotes from messier.txt to handle comparison
    private String removeQuotes(String text) {
        if (text.startsWith("\"") && text.endsWith("\"")) {
            return text.substring(1, text.length() - 1);
        }
        return text;
    }

    //convertRA function
    private double convertRA(String ra) {
        int hIndex = ra.indexOf('h'); //making parse format
        int mIndex = ra.indexOf('m');
        int sIndex = ra.indexOf('s');
        double hours = Double.parseDouble(ra.substring(0, hIndex));
        double minutes = Double.parseDouble(ra.substring(hIndex + 1, mIndex));
        double seconds = Double.parseDouble(ra.substring(mIndex + 1, sIndex));
        double decHours = hours + minutes / 60.0 + seconds / 3600.0;
        double degrees = decHours * 15.0;
        return Math.toRadians(degrees);
        //reference: https://stackoverflow.com/questions/34236175/degrees-minutes-seconds-to-radians-formula-not-working
    }
    //convertDEC function
    private double convertDEC(String dec) {
        int sign = 1; // constant for declination
        String workingString = dec;
        if (dec.startsWith("-")) { // if number is negative change sign to negaitve
            sign = -1;
            workingString = dec.substring(1);
        } else if (dec.startsWith("+")) {
            workingString = dec.substring(1);
        }
        int degIndex = workingString.indexOf('°'); // parse format
        int minIndex = workingString.indexOf('\'');
        int secIndex = workingString.indexOf('"');
        double degrees = Double.parseDouble(workingString.substring(0, degIndex));
        double minutes = Double.parseDouble(workingString.substring(degIndex + 1, minIndex));
        double seconds = Double.parseDouble(workingString.substring(minIndex + 1, secIndex));
        double decimalDegrees = degrees + minutes / 60.0 + seconds / 3600.0;
        decimalDegrees = decimalDegrees * sign;
        return Math.toRadians(decimalDegrees); // convert to radians
        //reference: http://www.stargazing.net/kepler/altaz.html
        //           https://stackoverflow.com/questions/5763841/convert-from-radians-to-degrees-in-java
    }

    // calculate absolute magnitude
    public double absoluteMagnitude() {
        double distanceLY = 1000* distanceKLY;
        return apparentMagnitude - 5.0 * (Math.log10(distanceLY) - 1.0);
        // reference: https://www.w3schools.com/java/ref_math_log.asp
        // https://en.wikipedia.org/wiki/Absolute_magnitude
    }

    @Override
    public int compareTo(MessierObject other){ // compare the magnitudes
        if (this.apparentMagnitude < other.apparentMagnitude){
            return -1;
        }
        else if (this.apparentMagnitude > other.apparentMagnitude){
            return 1;
        }
        return 0;
    }

    private String quote(String text) {
        return "\"" + text + "\"";
    }

    @Override
    public String toString() { // converts to strings to be displayed
        return messierNumber + ", " +
                quote(ngcNumber) + ", " +
                quote(objectName) + ", " +
                type + ", " +
                distanceKLY + ", " +
                constellation + ", " +
                apparentMagnitude + ", " +
                ogRA + ", " +
                ogDEC;
    }

    public String getMessierNumber() { return messierNumber; }
    public String getNGCNumber() { return ngcNumber; }
    public String getObjectName() { return objectName; }
    public String getType() { return type; }
    public String getConstellation() { return constellation; }
    public double getDistanceKLY() { return distanceKLY; }
    public double getApparentMagnitude() { return apparentMagnitude; }
    public double getRightAscension() { return rightAscension; }
    public double getDeclination() { return declination; }
    public String getOgRA() { return ogRA; }
    public String getOgDEC() { return ogDEC; }
}

