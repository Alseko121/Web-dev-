import { Component, OnInit } from '@angular/core';
import {Album} from "../album";
import {AlbumsService} from "../albums.service";

@Component({
  selector: 'app-posts',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: Album[];
  newAlbum: Album;
  loaded: boolean;

  constructor(private albumsService: AlbumsService) {
    this.albums = [];
    this.newAlbum = {} as Album;
    this.loaded = true;
  }

  ngOnInit(): void {
    this.getAlbums();
  }

  getAlbums(){
    this.loaded = false;
    this.albumsService.getAlbums().subscribe((albums) =>{
      this.albums = albums;
      this.loaded = true;
    })
  }
  deleteAlbum(id: number){
    this.loaded = false;
    this.albumsService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter((album) => album.id !== id);
      this.loaded = true;
    });
  }


}
