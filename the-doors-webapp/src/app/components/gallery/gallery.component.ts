import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-gallery',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})
export class GalleryComponent {
  images = [
    { src: 'https://clickamericana.com/wp-content/uploads/The-Doors-band-1960s-publicity-still-with-added-psychedelic-color-overlay.jpg', alt: 'Jim Morrison' },
    { src: 'https://www.classicposters.com/wp-content/uploads/2021/03/Doors.jpg', alt: 'The Doors Live' },
    { src: 'https://thisis-images.spotifycdn.com/37i9dQZF1DZ06evO19UBIk-default.jpg', alt: 'Album Cover' }
  ];
}
