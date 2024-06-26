<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# AI Chord Progression Generator
Building AI course project:
In this final project for the Building AI course, my AI idea is to create a Chord Progression Generator to use in music practice

## Summary

Musicians are always looking for new ideas to practice against or for songwriting inspiration. This project will allow users to generate a chord progression based on several inputted songs.
The user can input any number of sample songs from which they want to generate ideas. The model will then produce several chord progression ideas that the user can choose from, modify with variations (for example, changing a chord from sus2 to sus4, major to minor, etc.), then output a final version.

## Background

As a musician, it can be difficult to find new inspiration in songwriting or just creating new chord progressions to practice lead work against. This project provides that creative inspiration to break a musician out of a rut or let them make new progress in a boring practice routine.

## How is it used?

A web-based interface should prompt users to enter a song or artist name or specific URL to a hosted version of a song. Any number of songs can be entered to provide more sample data, however with too many dissimilar songs the output may become too randomized.
After inputting the example songs, the model generates 3-5 options of chord progressions with audio playback as well as written chord charts for each. The user can play each progression, drill into each, and refine with different chord voicings, change chord order and timing. 
Once the user is satisfied with their changes, they can choose output formats. They could produce a 3-5 minute "song" download, create a streaming loop to play via their pc indefinitely, or more.

## Data sources and AI methods

Possible data sources are available Spotify, Pandora, and Tidal data, Uberchord, and others

* [Spotify Datasets](https://research.atspotify.com/datasets/)
* [Uberchord API](https://api.uberchord.com/)

## Challenges

As a tool for inspiration or practice playing over looped progressions, this is a fantastic idea. However, the question raised by AI opponents has included "what is art?" Using AI to generate a song idea would put us into a gray area for sure. Is an idea generated by AI art? What about the human modifications made to the ideas?

## What next?

This idea needs a skilled technical team to understand how to build and/or reuse song model data. Existing models that detect and analyze chord progressions can be put to use. But a site design and architecture need to be created to begin work. I would need a programming team to help construct the site and really make this work.


## Acknowledgments

* [Uberchord API](https://api.uberchord.com/)
* [Spotify Datasets](https://research.atspotify.com/datasets/)
