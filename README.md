A visualization of covid19-related artworks made in different places of the words throughoout the time.



Introduction
============

Since the advent of the COVID-19 pandemic in early 2020, practicing artists and individuals with little previous art experience are expressing the effect of coronavirus on life in creative artworks and share a picture of them on social media. The output of their works usually indicates recurring themes such as the affective experience of isolation, the symbolic and material meanings of home, the importance of connection with digital technologies, and even social justice challenges like racism and domestic violence caused by COVID-19. These artworks usually manifest in the form of paintings, photographs, and various kinds of handicrafts. The collection of arts in these unprecedented times is extremely valuable as they reflect the day-to-day lives of people, their moments of happiness and sorrow in isolation, and generally their viewpoints and mental state in different phases of the COVID-19 pandemic. If collected, managed, and visualized correctly, this art collection can provide a valuable source of data for analyzing the psychological and sociological aspect of the “new normal”, give us a tool for predicting the emerging themes of the future, and preserve a collection for future generations who want to look back at Corona pandemic times. The artworks make this feasible especially because they depict events and emotions with a short time delay and can be linked to specific meta data like time, location, and demographic information.

Up to this date, the general impact of COVID-19 pandemic on the world of art has been discussed in press and blog posts. A handful of academic articles has investigated certain aspects of it, such as the potential of art-therapy for maintaining mental health during physical distancing, management of art museums amid the pandemic, and the effect of lockdown on the business of art auction markets, cultural tourism, and art performances. However, as far as we know, there has not been an effort to gather a dataset of COVID-19 related art-works and visualize them with the purpose of exploratory analysis from the sociological perspective. Probably the closest work to this proposal is Feng’s study on participatory online art practices in China and the pervasive surveillance and collaboration of the state on and with them.

In response to the gap mentioned above, we produced a sample COVID19-related art database in the form of an openly accessible website, and visualized the database based on the geographic and time information of the art data. We also ran a user study to inquire about the expectations of the potential users of the system, evaluate the website prototype, and gather feedback for further improvement of the database and visualization. The user-study results show that a geo-temporal visualization aligns with the expectation of potential users, and most of the users request more filtering and searching features in the database visualization to aid the exploratory analysis of the data. Our results also reveal that the visual encoding of COVID-art database in the form of geo-temporal mapping elicits new social science questions like the possibility and origins of bias in data, cultural differences in creation and sharing of art, and cross-country differences in the content of art-works. Our participants also indicated curiosity about the major themes emerging from the content of artworks, how they could be linked to different phases of the pandemic, different geographies, and the local and global political news.
![image](https://user-images.githubusercontent.com/19597430/123829355-6426e580-d8d0-11eb-97cc-b4c3f8131185.png)

[fig1: A screenshot of the COVID and ART database visualization. The users can explore data points (art pieces) based on their geographical locations and use the slider at the bottom of the page to alter the creation date. After hovering or clicking on each data point, a small window pops up which includes the title of art work or user name of the artist, the creation date, and a clickable hyperlink which directs the users to the original website containing the art piece. ]

Methodology
===========

In this section, we will explain our research questions and methodology for conducting this study.

Research Questions
------------------

Based on the premise mentioned in the introduction section, we started this project to answer the following two questions:

-   **RQ1**- What are the expectations of expert users from the visualization of a digital dataset of covid-related artworks?

-   **RQ2**- What are the suggestions of users for further improvement of the visualization in the next steps?

-   **RQ3**- What kind of questions our visualization invoked, which was otherwise obscured from the users’ sight?

In the first question, we define “expert users” as the individuals who might use the COVID-art database for answering a specific question, like researchers in the field of history, social science, public health, or psychology.

Methods
-------

We defined three phases for completing this project, which we will describe in detail under each subsection. This study design was inspired by Dr. Tamara Munzner’s paper, which suggests validating each phase of the study with a nested-model approach.

### Phase 1 \_ Creating a prototype of the database and visualization

The first step in creating a database of COVID-related artworks was to gather the dataset and clean it. To this end, we decided to focus on the publicly shared database on social media and available archives of art relevant to this effort. Using snowball sampling to find the co-occurring relevant hashtags, we came up with six hashtags as seeds of scraping data from *Facebook, Instagram, and Google Arts and Culture*. The hashtags are *\#covidart, \#covid\_art, \#covid19\_art, \#covid19art, \#covidart2020, \#covidartmuseum,* and *\#covidartchallenge*. We also used the *German Coronarchive database, the “Journal of a Plague Year” archive, and the “Urban Art Mapping” project*, all of which have collected COVID-related art and media in the form of a list of entries with no visualization. Since it is the prototyping phase of the project, we decided to work with a sample of 5364 data points for now and increase the database’s size in the next phases of the project. Each data point comprised a URL link to the webpage containing the art, the time of uploading the art piece, and its location. In the cases where the artwork missed some metadata like time and location, we assigned a random time or geolocation to them, just for the sake of making a viable visualization in the prototyping phase. This problem could be eliminated when creating the main database by focusing on data that possess both time and location. After preparing the sample database and cleaning it, we used the Plotly Python package and Mapbox tool to visualize the data points in the form of a 2D geographical map with a slider added to it to add the time dimension. We made a scattered-map of data, which allows the users to explore different locations and dates and see the artworks generated at that time and place. After clicking on each data point, a new tab will open, which shows the artwork on its original website. We could not directly show the art-piece photo on our website for copyright and ethical permission reasons. You can visit the final prototype at maryammokhberi.github.io/covidandart. Also, you can see a screenhot of the visualization in figure  [fig:figures/covidandartmap].

### Phase 2 \_ User-study

After preparing a prototype of our envisioned website, we arranged an informal user study session with five participants. All the participants were experienced in social science research and qualitative analysis. This session was comprised of three parts. At the beginning of the session, we asked the participants to fill out a **pre-session questionnaire**. Our intention was to validate the potential future users’ expectations from a covid-art database and make sure we understand their actual needs. Next, we gave the participants 20 minutes to **explore and manipulate the COVID and ART prototype website** and answer the potential research questions they had in mind. After spending enough time with the prototype, we finally asked them to fill a **post-session questionnaire** to know if this visualization has helped them develop new ideas and questions where they would not have otherwise formed. You can see the pre- and post-session questions below:

*Pre-session questions* Q1 \_ Imagine you have access to a database of all the artworks generated in the time of a pandemic. What kind of questions would you like to answer using this database? Q2 \_ Imagine we are making some data visualizations using this database and putting them on a website. What kind of data visualization themes would you like to see about this database? Q3 \_ What are your expectations regarding the interactive features of this visualization? i.e., what kind of tools would you like to have when exploring the data? *Post-session questions* Q1 \_ What new research questions come to your mind after working with COVID and ART visualization? Q2 \_ Do you have any feedback for improving the COVID and ART website and visualization?
![image](https://user-images.githubusercontent.com/19597430/123829722-b0722580-d8d0-11eb-8d10-e25f5a47e82f.png)


![fig2: A summary of second phase of the study.]

### Phase 3 \_ Fine-tuning and improvement of the website and visualization

After gathering the responses and feedback from the participants, which we will present and analyze in the next sections, we will improve the database and visualization based on the users’ comments.

Results and discussion 
=======================

Our participants gave us very valuable answers and feedback in response to the questionnaires in the user-study sessions. Their insightful input is summarized in table [tab:pre-session] and table [tab:post-session].

As you can see in table [tab:pre-session] about the pre-session questionnaire, the curiosity of expert-users in using a COVID-art database lies in many different directions, but the most recurring questions they have is about the reflection of emotions in the art pieces, and the main theme of arts in different phases of the pandemic. The other questions point out symbols of COVID in arts, most influential artists, trends of arts over time, demographics of artists and missing data, and finally, the alignment of artworks with perceived real-life experiences.

When it comes to the expectation of expert-users from the visualization encoding of a COVID-art database, our participants mentioned they would like to see a geographical map of most dominant themes in different periods of time, a time series of data points in each art theme, and a quick video or slideshow of the latest generated arts. In response to the question about the expected interactive features of a COVID-art database visualization, the majority of participants mentioned the option of seeing the data points at different times and locations. In addition to this factor, the expectations are about searching and filtering the data based on different features, previewing the art-images when working with data entries, and making new collages and posters using the database.

Table [tab:post-session] indicates the results of the post-session questionnaire, which we asked participants to fill after working with the COVID and ART prototype website. This table shows how our visualization triggers new questions in users’ minds, which they would not have necessarily asked if they had not seen the data points in a scattered map. The new research questions are about the imbalance of data points based on their location and potential reasons behind that, the similarity of COVID-related art themes in different parts of the world, and trends of different art genres based on their location and date. Besides these, a new question irrelevant to data location was about the way people’s personal image [reflected in the art pieces] challenges or complements the broader narrative of the pandemic that is not told in the mainstream media.

In table [tab:post-session] you can also see the participants’ feedback for further improvement of our visualization. Most users suggest adding more filtering features, adding encodings that support the exploratory analysis of the database (such as colour-coding the content and using line charts). They also encouraged us to give the user to see a preview of the art image on the same page as visualization when clicking on a data point. Lastly, we received feedback to include the information about COVID cases (number of active, recovered, and terminated patients) in different times and locations to be explored along with the COVID-related art database.

One of the points that came up in the users’ input is the potential bias in data and the possibility of misrepresentation of some communities in our scraped database. We acknowledge that our focus on English hashtags has induced a source of bias in the database. Another source of bias might be different cultural practices that make artists of certain regions more willing to public-sharing of their works compared to artists in other places. Another reason might be the lack of easy access to the internet, which leaves some artists out without the opportunity of entering their work into the pool. While the first issue can be eliminated by generating a more inclusive and comprehensive pool of hashtags before data-scraping, the last two reasons are beyond our control.

![image](https://user-images.githubusercontent.com/19597430/123830272-25ddf600-d8d1-11eb-97ae-9119e0eba924.png) ![image](https://user-images.githubusercontent.com/19597430/123830373-37bf9900-d8d1-11eb-845d-05f7bacffe6e.png)


[t!]

<span>c c</span>
 & <span>*Times mentioned*</span>
 & 1
(r)<span>3-4</span> & 1
(r)<span>3-4</span> & 1
(r)<span>3-4</span> & 1

& <span>*Times mentioned*</span>
 & 3
(r)<span>3-4</span> & 1
(r)<span>3-4</span> & 2
(r)<span>3-4</span> & 1
(r)<span>3-4</span> & 1
(r)<span>3-4</span> & 1

 [tab:post-session]

Limitations
===========

The limitation of this work is that we only focus on publicly shared artworks on social media, although there is a significant percentage of the artist who might not have shared their work publicly.

Also, downloading all the COVID19-related artworks, which are in the form of image data, and placing them on the server required a huge amount of processing memory and maintenance. Therefore we decided to only include the URL link to the original website of the artwork in our visualization. However, it is worth mentioning that copy-right and permission issues were another reason we did not directly include the images in our map and used the URL links instead. We hope to solve this issue by officially partnering with data sources like Instagram and Facebook and using their APIs to extract better quality data and place the images of artwork on our website.

Another limitation of our current work is that the whole visualization code, which is relatively heavy, is transformed from Python code to HTML before deployment on the prototype website. This issue has made the website a bit slow but can be solved in the next steps by using the Python code in the back-end of the website, instead of using HTML to show the visualize.

Conclusion 
===========

In this project, we collected a sample dataset of publicly shared COVID-related artworks from social media and online archives and made a prototype visualization of the data based on the date and location attributes of the artworks. We also ran a user study to find out the expectations of expert users from the visualization of a digital art collection and collected feedback for further improvement of the system in the next steps.

The results of the user-study session inform us about the expectations of potential users from a COVID-art database, validates our prototype visualization, and suggest feedback for further improvements of the system. By looking closely at the participants’ responses, we can answer the research questions we defined at the beginning of the methodology section. First of all, we know that expert users might have various intentions and research questions when working with the COVID-art database. Second, we learned that the expectation of most users about the visual encoding of such a database aligns with our prediction and our prototype, namely, visualizing the data points in the form of a scattered map with a temporal dimension. In addition, we figured out most users expect some filtering and searching tools added to the visualization. Lastly, we learned that visualizing the COVID-related artworks in the form of a scattered map evokes new ideas and questions in researchers’ minds, and these new ideas mostly arise from the relationship of artist location and the content and quantity of the produced art. Encouraging expert users to pay attention to the location-related attributes of data is important, especially because it makes them take cultural and language differences into account when analyzing the data, warns them about bias and missing population in a dataset, and prevents them from forgetting about the marginalized communities. This will eventually lead to a creation of more comprehensive research questions by researchers in the field of humanities, fairer policy makings by world leaders, and a more realistic narrative of the COVID-19 pandemic.

