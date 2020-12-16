# Climate Change Disinformation on Twitter
Author: Andres De La Fuente

University of Washington, 2021

## Abstract
This analysis explores the possibility of using features related to user accounts on Twitter in order to identify
bot activity. Specifically, the goal is to differentiate users based on features which have been identified
as useful for this purpose by other researchers, and subsequently to analyze differences in the posts made by 
users in the identified 'suspicious' group versus the overall patterns. Some of the user features employed in
identification of suspect accounts are:

- The age of the account when making the post
- The posting frequency of the account
- The percentage of numbers in the account's name

Some of the features analyzed to observe differences in posting behavior are:
- The use of hashtags
- The use of URLs
- A positive / negative sentiment breakdown

The results of some relatively limited examination on these features reveals promising findings about the
suspect accounts, as they differ from the rest in ways that match intuitive expectations of bot behavior.

## Data Used
[This is the dataset used](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/5QCCUU) in my
analysis.

*For a breakdown of how to access the data and set it up the way I did read the Data section of the 
Report python notebook*

This data is published under the CC0 license, so it is free to use in this context.

## References
The following are the resources referenced to decide on user features to target and for some background:

- [Political Astroturfing in South Korea](https://www.researchgate.net/profile/Junghwan_Yang2/publication/317290047_How_to_Manipulate_Social_Media_Analyzing_Political_Astroturfing_Using_Ground_Truth_Data_from_South_Korea/links/59305a9ca6fdcc89e7844440/How-to-Manipulate-Social-Media-Analyzing-Political-Astroturfing-Using-Ground-Truth-Data-from-South-Korea.pdf)

- [Russian Political Disinformation](https://secondaryinfektion.org/)

- [Detecting the Use of Multiple Accounts](https://onlinelibrary.wiley.com/doi/abs/10.1002/cpe.4013)

- [Common Signs of Bots](https://blog.mozilla.org/internetcitizen/2018/01/08/irl-how-to-spot-a-bot/)

