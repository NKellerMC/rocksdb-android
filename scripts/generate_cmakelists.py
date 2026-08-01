from pathlib import Path

cmake = r'''cmake_minimum_required(VERSION 3.10)

project(rocksdbjni)

add_library(rocksdbjni SHARED
    ../rocksdb/java/rocksjni/rocksjni.cc
    ../rocksdb/java/rocksjni/backupenginejni.cc
    ../rocksdb/java/rocksjni/cache.cc
    ../rocksdb/java/rocksjni/checkpoint.cc
    ../rocksdb/java/rocksjni/columnfamilyhandle.cc
    ../rocksdb/java/rocksjni/comparator.cc
    ../rocksdb/java/rocksjni/env.cc
    ../rocksdb/java/rocksjni/iterator.cc
    ../rocksdb/java/rocksjni/options.cc
    ../rocksdb/java/rocksjni/rocks_callback_object.cc
    ../rocksdb/java/rocksjni/slice.cc
    ../rocksdb/java/rocksjni/write_batch.cc
)

target_include_directories(rocksdbjni PRIVATE
    ../rocksdb/include
    ../rocksdb
    ../rocksdb/java/rocksjni
)

target_link_libraries(rocksdbjni
    rocksdb
    log
)
'''

Path("CMakeLists.txt").write_text(cmake)
print("CMakeLists.txt gerado.")
