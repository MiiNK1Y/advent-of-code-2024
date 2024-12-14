# THE IDEA TO SOLVE P2
---

# NB!!: FAULTY, INFINITY LOOP
# NEED TO GET THE RULE-SET THAT COMPLIES WITH THE CURRENT PAGE UPDATE

## The general draft
---
- First, sort the rules by the rules themselves in a list.
    - remove duplicate numbers, and make sure they are in the correct position.

- Second, sort the "updates" based on the sorted rules.
    - go page for page in the updates, and check that their position is similar to the their position in the sorted rules.

## The more detailed breakdown
---
### Sorting the rules
1. Go through the first rule in each rule-pair;
    - and check if they have any "first-rule" to obey.
        - if there is no first-rule to obey,
            - then we know that this number should be the first rule in the array.

    1.2. If there is a "first-rule" to obey;
        - then we need to find out how many "first-rules" there are we need to keep tab of.
            - when we know how many "first-rules" there are,
                - we need to know if any of them is already in the new array.
        - if all the "first-rules" are already in the array,
            - then we can just add this one.

    1.3. If there are multiple "first-rules";
        - and some of them are not in the array,
            - then we need to skip this one for now, and focus on the next one to check.

    1.4. Loop this process until we have sorted all the rules.
        - double check the result,
            - by going backwards in the array and checking both first-rules and second-rules.
                - if the rules comply in both directions, we have the completed array.

### Matching each update with the sorted rules
Since we now have sorted the rules;
    - we know how to sort the pages in the updates correctly based on the array of the sorted rules.

2. go over every page in each update,
    - and match their position to make it as similar to the rules-array.

    2.1. If the page is not in the rules-array,
        - save that page for last, since it probably should be at the end of the sorted update.

    2.2. By looping over the rules-array for each update,
        - find a matching page, and insert it into the sorted update.

            - do this for every update, and the pages should be in correct order.


# NEW IDEA THAT SHOULD VOID THE INFINITY LOOP
---
- Get the rule sets that matches the numbers in the pages, and not the whole rule-set at a time.
    - generate new rule set based on the pages / numbers found in the updates.
