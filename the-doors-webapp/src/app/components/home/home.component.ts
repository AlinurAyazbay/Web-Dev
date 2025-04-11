import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  images = [
    { src: 'https://cdn-images.dzcdn.net/images/artist/94d0bdcebb2840d36ccf63e9edde540a/500x500.jpg', alt: 'Jim Morrison' },
    { src: 'https://i5.walmartimages.com/seo/The-Doors-Blu-ray_3e70df09-7f61-4ffc-90b7-fd855b367891.e5f7540a37adaefa0f289b864f0d227a.jpeg', alt: 'The Doors Live' },
    { src: 'https://static.tvtropes.org/pmwiki/pub/images/1000009772.jpg', alt: 'Album Cover' }
  ];
}
