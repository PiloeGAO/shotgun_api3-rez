<!-- Template: https://github.com/othneildrew/Best-README-Template/blob/master/README.md -->

<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">shotgun_api3 Rez Package</h3>

  <p align="center">
    A shotgub_api3 rezified package based on the official builds.
    <br />
    <a href="https://github.com/piloegao/shotgun_api3-rez/issues">Report Bug</a>
    ·
    <a href="https://github.com/piloegao/shotgun_api3-rez/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project allow you to have a ready to use rez package for the FLow Production Tracking python api (`shotgun_api3`). On build/install, the package will download the version matching the one mentionned in `package.py` from the official website and will create all the appropriate aliases.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This rez package was tested with the following versions:

* Python 3.10+
* Rez 3.1.1+

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how to set up the project locally and get a local copy up and running.


### Installation


1. Clone the repository:
   ```sh
   git clone https://github.com/piloegao/shotgun_api3-rez.git
   ```
2. Run the rez build/install command:
   ```sh
   rez build -ci
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once installed, you can then start a rez environment with the `shotgun_api3` package and run python :
    ```sh
    rez env shotgun_api3
    python
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Run [black](https://github.com/psf/black) to ensure formating is correct
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Leo Depoix - [LinkedIn][linkedin-url] - [leodepoix.fr](http://www.leodepoix.fr)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Proudly used in production by:

* [Piktura](https://www.piktura.fr/)

_If you are using this package in your studio, contact me on [LinkedIn][linkedin-url] and I will update the list with your name and a link._


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/piloegao/shotgun_api3-rez.svg?style=for-the-badge
[contributors-url]: https://github.com/piloegao/shotgun_api3-rez/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/piloegao/shotgun_api3-rez.svg?style=for-the-badge
[forks-url]: https://github.com/piloegao/shotgun_api3-rez/network/members
[stars-shield]: https://img.shields.io/github/stars/piloegao/shotgun_api3-rez.svg?style=for-the-badge
[stars-url]: https://github.com/piloegao/shotgun_api3-rez/stargazers
[issues-shield]: https://img.shields.io/github/issues/piloegao/shotgun_api3-rez.svg?style=for-the-badge
[issues-url]: https://github.com/piloegao/shotgun_api3-rez/issues
[license-shield]: https://img.shields.io/github/license/piloegao/shotgun_api3-rez.svg?style=for-the-badge
[license-url]: https://github.com/piloegao/shotgun_api3-rez/blob/master/LICENSE.txt
[blender-url]: https://www.blender.org/
[linkedin-url]: https://linkedin.com/in/piloegao