+++
title = "The Algerian Linux Distribution hackathon experience"
description = "Insights of my first ever hackathon"
tags  = ["linux", "hackathons", "algeria"]
release-date = "2026-04-21"
draft = false
+++

The First Ever [Competition/Hackathon][competition-link] to create an "Algerian" Linux distribution.

It was really an Algeria's first. It was huge, I was hearing about it in every university club, Algerian server/community related to Linux, and whatnot. This is the first ever hackathon of such scale that I ever entered into, and it was certainly an experience.

The point of this blog/article is to reflect back on the competition, what happened during it, and, of course, the (catastrophic) aftermath that came with it.

## A hackathon never seen before

Hackathons are getting more and more popular in Algeria. However, most of hackathons are organized by university clubs (such as [MicroClub][microclub], with modest, or often non-existent prize pools. Moreover, they are usually axed towards making some random slop software that goes to nowhere.<br>
Generally we'd see some sort of Software-as-a-Service (SaaS), usually consisting of a dashboard, some sort of backend/database combo, and of course AI integration because that's what people can only think about

This was genuinely different. The concept was really novel and it called for a really small nice in Algeria: "Hardcore" Linux users/Linux enthusiats. People that are confident enough in themselves to say: "yes, I can build a whole distribution from zero!"

### A quick note about the prizes

While I didn't enter for money as a first objective (I actually entered with the mindset that I'm not gonna make it to the podium), a lot of people were genuinely motivated by the pure monetary value of the prize pool.

If you are unaware, the Algerian Dinar `DZD` is **not** convertible, and it is *by choice* of our government, to our despair. Most things are subsidized by the same government, of course, but still, this essentially means the value and power of the currently is close to zero.

All the value of the currency is tied to black-market rates (since the banks are useless, and the "official" exchange rate of dinar means absolutely nothing). In short, that huge cash prize is worth:

- **1st place**: `~10500USD`
- **2nd place**: `~6300USD`
- **3rd place**: `~4200USD`

> FYI. The dinar (at the time of writing) is now convertible at a rate of `278DZD => 1EUR`, or
> `252DZD => 1USD`. The rate is getting higher and higher every time!

If this might seem low (which it isn't, this is huge money for any hackathon, really), it's a HUGE amount of money that most Algerians would use to kickstart a project, or get married, or whatever. _I cannot stress enough_ how that for most participants, this is "life-changing" money.

[microclub]: https://microclub.info
[competition-link]:https://www.univ-saida.dz/fr/le-premier-concours-de-creation-dune-distribution-linux-algerienne/


---

## A really honest committee

The people behind the hackathon are really amazing. The CNLL, which stands for "**C**omité **N**ational des **L**ogiciels **L**ibres" (translated: National Committee of Free Software) are, in short,a bunch of Math/Physics/Computer Science teachers that found similar interest in Free Software (with free as in *freedom*)

They strongly believe in the free software, and they slowly over the years made the whole [University of Saida][usmt] run on free *self-hosted* software! We did a tour of their administration. They are really sold on the idea of it, no sight of Windows or anything!

They provide for *all* students a [NextCloud][nextcloud], with an e-mail address, a private storage bucket. They also host a custom mastodon instance for uni news, no Facebook group or borked Telegram channel (something that I blame my university for doing to this day)

Overall, I believe they are really well-placed to host and be the judges about this competition.

[usmt]: https://univ-saida.dz
[rhel]: https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
[nextcloud]: https://nextcloud.com

---

## Some interesting challenges

On the d-day, after finishing check in and some meet and greets with the participants, we were walked into a conference room. On it some 50-year-old looking person started explaining to us the concept of the competition, the timeline/schedule, where we are going to hack... all the fun information.

The hackathon was actually split up into 4 challenges, with a "fifth" challenge or phase being to make a presentation about our final product, and what we managed to get out of it.

I won't really judge here the relevancy of the challenges because they were more or less in-line with the objectives of the distribution: a flexible, deployable minimal system that was "Algerian" (oh man more on that later).

For the actual challenges, here they are, in order

1. **Build a custom Linux kernel from source**: This includes all the typical steps of making your own kernel. Gentoo users (which I was daily-driving at the time) will feel right at home.
    - You would need to configure it for some piece of specific hardware they requested. This mostly required a quick dance between `lspci` and `make menuconfig`, nothing more really.
    - You were asked to build it, again nothing special, a quick `make -j16` and off you go. 
    - The final part was making sure it's a bootable kernel. You'd install it using your distribution utility, make sure you'd ask `dracut` or whatever to create the `initramfs`, and boot in.

2. **Make a minimal bootable `.iso`**: There's again nothing special. A bunch of `xorriso`, `mkfs`, and whatnot, I don't remember exactly what we did, I followed a guide that I lost really.

3. **Turn the live ISO into a running system**: It's mostly about preparing some scripts on the ISO and running them. Some teams (including mine) also made other ISOs and environment using [`debootstrap`][debootstrap]. This technically isn't "Linux-From-Scratch", but was still considered right (after all it would be insanity to maintain our own package repository...)

4. **Auto-deploy said ISO in a virtual environment**: I wasn't really involved in this step, so I don't have any remarks to say about this. I was pretty much out by then, and went to sleep.

For **~68 hours** of time, we got a pretty generous time frame to work and hack. I'll skip you all the people that tried the wrong things, and the catastrophic failures of the people that were driven by the money prize.

We were provided really capable machines (I believe with some i7-12700k, 32GB of ram, SATA SSDs...), so there wasn't much bottlenecking regarding compiling tasks. Decent Internet (120MB/s) was also provided, which is nice.

[debootstrap]: https://wiki.debian.org/Debootstrap/

---

## The aftermath

It was, bad. *Really* bad. I cannot explain the extents of how this whole competiton became the most misinterpreted event in all of Algeria.

During the closing ceremony, the first thing that happened was a talk from Kamel Baddari, the Minister of Higher Education and Scientific Research of Algeria at the time. It was mostly about the fact that algeria needs software independence, and how free software will guide us to a better country stability, the evil of Microsoft Windows, etc.

We then were called to hold huge plastic checks with the value of our promised prize written in huge **bold** numbers, for the show, and for the news channels and facebook groups to feed on. Mostly a lot of show and not much of actually interesting talk.

### The nationalists screaming

The first problem in a lot of people's interpretation of what's an "*Algerian* Linux distribution" is in my opinion really wrong. Algerian people are **huge nationalists**, to the point that it skewed all the goal of the competition.

A Linux distribution doesn't have a nationality. A Linux distribution isn't "tied to a country" (aside from a few edge cases). However, many people thought our project is about slapping the Algerian flag and a few references to the country or something. It's wrong.<br>
In addition to that, a lot of the news coverage about the topic --- which to be fair tried its best --- was interpreting the outcome of the competition as "making an Algerian Windows", which is completely against the point of our project; Linux is about being open, having full control, fine tuning it to your preferences, ...

Here are (in my opinion) more interesting ideas to actually make this distribution Algerian:

- Native support for all spoken languages in Algeria. Arabic and French are well supported, English too. However [Tamazight][tamazight] (The language of the Amazight people, aka Kabyles, aka Berber, and branched off in many subgroups) is another story<br>
I wouldnt' say that making a whole bunch of translation files is easy and all, however preliminary support (or promise to) would have been a strong talking point

- Try to cater to existing infrastructure software. A lot of Algeria's administration runs on **Windows XP** of all things, with a shitload of legacy old software. Bundling of such legacy software more straightforward would have been IMO a much better selling point (I am sure 50+ year old social workers would NOT love to tinker with [Wine][wine])
    - There are *some* places were Windows 10 (only 10. 11 sucks anyway), however it's always non-activated copies, and it's always running the same legacy software.

- More innovation in computer literacy. Another target of this distribution was to be massively deployed in computer rooms of high schools and faculties. Having some sort of adapted tutorials (perhaps in local languages/dialects), or software catered towards specific use cases (like saying a "Algorithmics and Data structures ISO") would be really useful. A teacher can then come to the computer room, deploy the needed image with let's say a prepared C compiler toolchain and a text editor, and just put it on all the PCs in the room's LAN.

[tamazight]: https://en.wikipedia.org/wiki/Kabyle_language
[wine]: https://wine-hq.org

### The prize "drama"

Nobody really dramatized, but I really don't like the scummy moves the sponsors pulled off here. This is an issue with a lot of hackathons that feature prizes (either cash or whatever) across the world, but *specifically* in Algeria. There are many incidents such as the [InnovPost][innovpost-incident] (warning this is gonna take you on LinkedIn), and others (feel feel to [contact me][contact] and tell me about your experiences to get them listed here!

[innovpost-incident]: https://www.linkedin.com/posts/ikram-dadoune-1b5080233_hackathon-algerieposte-ooredoo-activity-7375130923668901888-fSwS/
[contact]: /about

First of all, they handed out prizes **3 months after the competition ended**. We wrapped up everything by November 21st 2024, but the day the prizes got handed out was the **Febuary 28th**! To make things worse it was the day before Ramadan.<br>
For people not living directly in the vicinity of Saida, like me, living in Algiers, this equals to **450KM** of distance (and I don't drive, so that burden was on my poor dad). It was a really badly timed day. A lot of participants resorted to taking taxis at exorbitant prices, or whatever means suited them best.

Prizes were promised for the top 3 podium (as you can see above). The podium being *teams* (not individuals, team sizes 2-4). Well, here's what happened for each of the 3 places:

For people in **1st place**: (which includes my team, with 3 other people) we got cut 4 equal cheques dividing the promised sum of 2.5 million DZD (amounting to) 625 thousand DZD each. Fair game. They were handed out by Sonatrach if I remember correctly.

For the team in **2nd place** --- a team of three --- The designated sponsor was meant to be Djezzy, a Telecom operator. Instead of giving out cheques, they gave out "prizes", consisting of:

- A Decent Laptop/Notebook from Asus I believe. 11th gen Intel i5, 8GB of ram (yes, only 8), 256GB (again yes only 256GB)
- A Maxed out Samsung Galaxy S24 Ultra (512GB model, colors vary)
  
The big issue is that if you resell these two, assuming that you resell them at the best prices (you *wont*), they can get a maximum yield of ~310 thousand DZD *each*. For three people, that is only 930K/1.5M of the cash prize; only **~62%**.

The team in **3rd place** got ripped off the hardest, by only getting that same laptop model. Each member should have gotten 250 thousand DZD each, they got a gift with the absolute maximum value of 110 thousand DZD --- less than *half*.

As much as I want to give them the benefit of the doubt, they probably planned that all the teams will have exactly four people, and in this case the picture doesn't look as bad, 1.2M/1.5M (still a missing **25%**). I am sure that when they saw that only 3 people are in the team, they said "you know what just refund the 4th gift bundle and give them that". That is really deceptive.

It wouldn't have been as bad if it wasn't for the fact that when confronted (the same day as they handed out these prizes), the sponsors representatives doubled down on this and said "we actually gave you more than what you should have gotten". We just gave up and stopped begging some corporate people about this.

### Taking the project forward

Regardless of the prizes, every participant actually wanted to take the project forward, and perhaps actually make it happen, and start a free software revolution in Algeria! This is some really blissfull thinking right here.

The truth is, people got busy with life; Most of the students needed to actually get back to preparing their exams, other non-students went back to working, or in the case of one, go back to high-school (the youngest participant, and the only minor besides me at the time).

We created a WhatsApp (yes, WhatsApp, very hypocritical for people working on a free software project) group, with around 45 members, me included. It was actually created to discuss when we would be getting our prizes, but after we shifted the purpose of it to discussing how to actually make the distribution a real thing.

However, we needed effort from *our side* and the *CNLL* side (or any sort of official entity that could relay us with the government), we didn't want to work and be driven by "just passion", especially for a more-or-less nation wide project, the undertaking needed would be huge.

I also want to blame it on people not fully in the free software idea, but who am I to speak, I'd rather not judge people's inner thoughts and beliefs here.

---

Overall, it was a really fun experience! I am really glad I participated to this hackathon, it was a great time meeting other people that love Linux, nerds just like me. While I am not happy with the outcomers of it, I don't regret any bit of it.

But really, it's a bunch of wasted effort that will probably go to waste. What are hackathons in Algeria anyway.

*<p style="width: 100%; text-align: right;">- nferhat</p>*
